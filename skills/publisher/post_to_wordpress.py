import sys
import json
import time

def publish_mock(title, content, tweet_text):
    """
    WordPressのREST API連携とX(Twitter)への投稿を行うモック関数。
    実際には、WordPressへHTTP POSTリクエストを送り、XのAPIを叩いてツイートする。
    """
    print("WordPressへ通信中...")
    time.sleep(1) # 通信をシミュレート
    
    # WordPress投稿結果のモック
    wp_result = {
        "status": "success",
        "action": "draft_saved",
        "post_id": 1042,
        "preview_url": "https://twi-soccer.com/?p=1042&preview=true"
    }
    
    print("X(Twitter)へ通信中...")
    time.sleep(1)
    
    # X投稿結果のモック
    x_result = {
        "status": "success",
        "tweet_id": "1893478912341",
        "posted_text": tweet_text
    }
    
    # 結果をファイルに保存
    with open("draft_result.txt", "w", encoding="utf-8") as f:
        f.write(f"=== WordPress Draft ===\nTitle: {title}\nURL: {wp_result['preview_url']}\n\n")
        f.write(f"=== X(Twitter) Post ===\n{tweet_text}\n")
    
    # 結果を出力
    final_result = {
        "wordpress": wp_result,
        "twitter": x_result,
        "message": "下書き保存とSNS告知の連携テストが完了しました。結果は draft_result.txt に保存されました。"
    }
    
    print(json.dumps(final_result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "No Title"
    content = sys.argv[2] if len(sys.argv) > 2 else "No Content"
    tweet = sys.argv[3] if len(sys.argv) > 3 else "新しい記事を公開しました！ #サッカー"
    
    publish_mock(title, content, tweet)
