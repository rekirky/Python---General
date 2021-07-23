data = {
    "object": "page",
    "entry": [
        {
            "id": "<PAGE_ID>",
            "time": 1458692752478,
            "messaging": [
                {
                    "sender": {
                        "id": "<PSID>"
                    },
                    "recipient": {
                        "id": "<PAGE_ID>"
                    },
                    "timestamp": 1458692752478,
                    "message": {
                        "mid": "m_1457764197618:41d102a3e1ae206a38",
                        "text": "hello, world! from reply message",
                        "reply_to": {
                            "mid": "m_1fTq8oLumEyIp3Q2MR-aY7IfLZDamVrALniheU"
                        }
                    }
                }
            ]
        }
    ]
}

class DeterminePayload:
    
    def __init__(self, data) -> object:
            self.data = data

    def get_values(self, *args):
            
            result = []
            
            data = self.data if len(args) == 0 else args
            
            if isinstance(data, dict):
                for v in data.values():
                    print(v)
                    result.append(v)
                    if isinstance(v, dict):
                        result.append(self.get_values(v))

            elif isinstance(data, list):
                    for list_items in data:
                        self.get_values(list_items)
                    result.append(data)    

            return result


exists = DeterminePayload(data)
print(exists.get_values())