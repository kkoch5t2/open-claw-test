import sys
import json

def scrape_mock_info(topic):
    """
    指定されたトピックに関する詳細情報をスクレイピングするモック関数。
    実際には、ここで複数の海外サッカーニュースサイトからHTMLを取得・パースして情報を収集する。
    """
    mock_info = {
        "topic": topic,
        "scraped_sources": [
            "https://mock-soccer-news.com/article1",
            "https://mock-sports-weekly.com/news2"
        ],
        "extracted_facts": [
            f"{topic} に関する信憑性の高い情報筋によると、水面下で交渉が進行中。",
            "ファンからは期待と不安の声が入り交じっており、SNSでのエンゲージメントが非常に高い状態。",
            "過去の類似事例と比較すると、成功確率は60%程度と専門家は分析している。"
        ]
    }
    
    print(json.dumps(mock_info, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    # 引数としてトピック名を受け取る
    topic_query = sys.argv[1] if len(sys.argv) > 1 else "デフォルトのサッカートピック"
    scrape_mock_info(topic_query)
