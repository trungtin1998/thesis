curl -XPOST "192.168.255.200:9200/_search" -H 'content-type: application/json' -d '
{ "query": {
        "bool": {
            "filter": [{
                "match_all": {}
            }, {
                "match_phrase": {
                    "event.code": "7045"
                }
            }, {
                "match_phrase": {
                    "winlog.event_data.ImagePath": "%SystemRoot%\\PSEXESVC.exe"
                }
            }, {
                "range": {
                    "@timestamp": {
                        "gte": "2020-05-10T15:59:56.888Z",
                        "lte": "2020-06-09T15:59:56.888Z",
                        "format": "strict_date_optional_time"
                    }
                }
            }]
        }
    }
}'

