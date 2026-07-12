import json
import random

def fetch_mock_trends():
    """
    海外サッカーのトレンド情報をモックとして返す。
    実際にはTwitter APIやGoogle Trends、RSSフィードなどをここで巡回する。
    """
    mock_trends = [
        {
            "keyword": "レアル・マドリード 移籍",
            "volume": random.randint(50000, 100000),
            "summary": "若手有望株の獲得に動いているとの噂がSNSで急上昇中。"
        },
        {
            "keyword": "プレミアリーグ 誤審",
            "volume": random.randint(30000, 80000),
            "summary": "昨晩の試合でのVAR判定を巡り、現地メディアやファンの間で大激論。"
        },
        {
            "keyword": "日本人選手 ゴール",
            "volume": random.randint(40000, 90000),
            "summary": "欧州リーグで日本人ストライカーが劇的な決勝ゴールを決め、現地紙で最高評価を獲得。"
        }
    ]
    
    print(json.dumps(mock_trends, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    fetch_mock_trends()
