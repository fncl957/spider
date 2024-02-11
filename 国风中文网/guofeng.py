import requests
import base64

'''获取每一个章节链接'''
def get_title_url():
    cookies = {
        'YUEDUDYAMIC': '430a12725ec1db6093e555d0984f020199639472',
        'YUEDU_V_DID': '1707395327283714',
        'NTESYUEDUSI': '6C1C6D50A479DA8843EC7E4E607ABE4F.hzabj-yaolu56.server.163.org-8010',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'YUEDUDYAMIC=430a12725ec1db6093e555d0984f020199639472; YUEDU_V_DID=1707395327283714; NTESYUEDUSI=6C1C6D50A479DA8843EC7E4E607ABE4F.hzabj-yaolu56.server.163.org-8010',
        'Referer': 'https://guofeng.yuedu.163.com/newBookReader.do?operation=catalog&sourceUuid=357452d4273a4cbc9db4824a4e904a64_4',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'operation': 'info',
        'sourceUuid': '357452d4273a4cbc9db4824a4e904a64_4',
        'catalogOnly': 'true',
    }

    response = requests.get('https://guofeng.yuedu.163.com/newBookReader.do', params=params, cookies=cookies, headers=headers)
    return response.json()


'''循环爬取每个章节并保存'''
def get_content():
    i = 1
    for article_uid in article_uids[1:]:
        cookies = {
                'YUEDUDYAMIC': '430a12725ec1db6093e555d0984f020199639472',
                'YUEDU_V_DID': '1707395327283714',
                'NTESYUEDUSI': '6C1C6D50A479DA8843EC7E4E607ABE4F.hzabj-yaolu56.server.163.org-8010',
            }

        headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                # 'Cookie': 'YUEDUDYAMIC=430a12725ec1db6093e555d0984f020199639472; YUEDU_V_DID=1707395327283714; NTESYUEDUSI=6C1C6D50A479DA8843EC7E4E607ABE4F.hzabj-yaolu56.server.163.org-8010',
                'Referer': 'https://guofeng.yuedu.163.com/book_reader/357452d4273a4cbc9db4824a4e904a64_4/8de85a872d904a94a57a24dc907e35d9_4',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        params = {
                'sourceUuid': '357452d4273a4cbc9db4824a4e904a64_4',
                'articleUuid': article_uid,
                'bigContentId': '8796093024106612419',
            }

        response = requests.get('https://guofeng.yuedu.163.com/getArticleContent.do', params=params, cookies=cookies,
                                    headers=headers)

        encoded_str = response.json()['content']
        decoded_str = dec(encoded_str)
        print(decoded_str)
        with open(f'龙霸帝疆/第{i}章.html','w')as f:
            f.write(decoded_str)
            i += 1
            f.close()


'''解密返回的章节密文'''
def utf8to16(data):
    return bytes(data).decode('utf-8')


def dec(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = utf8to16(decoded_bytes)

    return decoded_str


#
if __name__ == '__main__':
    ## 获取article_uids
    # response = get_title_url()
    # datas = response['catalog']
    # article_uids = []
    # for data in datas:
    #     secId = data['secId']
    #     article_uids.append(secId)
    # print(article_uids)

    article_uids = ['6e7cace3c8d1459a9e7302204231215d_4', '8de85a872d904a94a57a24dc907e35d9_4', '2597df6e8d6c459d9d516621405acbc6_4', 'f77367ffec38494a8113f84de31a3e9f_4', '05e4d7eb75554113867d03799b5959d9_4', 'a0f42cc0d687490a9b30a3fe8810d194_4', 'b3c260354ed04e9aa4900db36ca5aaf0_4', '3e71440eb6c3418e8d3c8524bbcbda2e_4', 'f27e42a5a97648ad8ff9f5bc0c1a7167_4', '23024e7e13cb42ed9122c268144a6bd7_4', 'bf02093baf95481bac4c3a9bfee3f0d0_4', 'b2d920bf72e84c04bf7a8ec9b94e7171_4', '2617a2338da546b9af5e052d5e8542fc_4', '85b32a9109f443d69a579aad61b99a10_4', '0c974cf483014bfc937c6a9d4ac91cb1_4', '41fd8d36e2a941979287681ecd54deac_4', '49b2f35523744835ac4ca604c661e5d4_4', '6749c0070ea94e1a8e03bc37efb0001b_4', '49796b46d2de46318bee73a3a82f85ca_4', '73d81ea457aa430e96cf786eb5e8cc48_4', 'ba8803f72d014989b060c7ae092df945_4', '396bca37619841cbaaec4a3b6e51e9fc_4', '922dede2883f439482e2026bae431314_4', 'f29b24ad58054250b7b347fb5e1f67b0_4', '3f94b999264d407b90a2c2b27cc005f7_4', 'b8560b2abdc84383b7b3e69a3a4fad7b_4', 'bdddcd9f1c224aae98db8a207fd07273_4', '8c728f2bca37441bb7fc4f5dfc8c1678_4', '7574e780c3934fe083a696f90176444e_4', '5a1e9f4a585544a0868cb8513a5ba973_4', 'a69689b16431452ab983776f822798aa_4', 'ba4368964cb54d08905b62a5baf5f10f_4', '599afcb7aac84233a356a86e67c50a74_4', '3b0f29481b1848bf80cbbc72cd34ecb1_4', 'e66550ecba174d5780c0dd27c6d8bb3d_4', '4d5d447d7262422dad3cfcb032ab9b59_4', 'a3e27b5eff3a47e2bfeda42bcea4d9fc_4', 'd4c3951f6da74d5ab37bca56db93bf6d_4', 'b68ed9515e0345b8aeb046d50183d0b3_4', 'a28068535dad408b88fa891017ba2bb0_4', '8a5acde6d76e4800b6b4023a5d6989ff_4', '5e060c66a19a4452b979011d1fef4cb7_4', 'd43bcc6d041e478ab610e0650de7c11b_4', '19fbb94c76894313b5cbf3dc510475e3_4', '12c42c949b444ca7894903975a15644f_4', 'a98c60acd148465e916775f8bfc67693_4', '8cb4975fdad94350810b50cf7663f1a0_4', 'c3ffc7a050e84ee8a6a30dd06b798fe5_4', '69678b7cdb38485ba90d9be30cda4856_4', '35f5c9be47cb456cacba4b3f071a058a_4', 'ca43a49aaa1a4c37909c4c123f065b8c_4', '9f654f1ff0cf4a21a550459140ceb8e2_4', '80a9e46cb4e9400db265423ed7376664_4', '52e0c394978c451cac58369dd9a57c82_4', '1fb9f96e876844b8bbe65ff72d05e035_4', 'c8c6bdc8713e49069015f80f8fb4a43f_4', '36135a9117fa4319a2556a6f5728a653_4', '180a8cc4097640e7809b6b85554701da_4', '5fc019328a3147c99d5b9c9168eaa9f4_4', '267936ef3285478998cad1832327ceb3_4', '4986808c24a347cdbc7e1c2c458b74c9_4', '02fcd839a7dd43318a0b56a5139112c1_4', '3a2d875b03f5446facb68f09118727f0_4', '32eb10ddc5b64c43b2f7334e897b6334_4', '6eb3ecf34be24107a1c369648c5932b1_4', '85c7404df5af4b64a6b136acfd794908_4', '86b97b668e874268afc25504f6704fb9_4', 'd77602e901a14836a172fec80cab234f_4', '577cd3b220a74197bec649135fe9b535_4', 'a48932c62dea42ff952549718947b194_4', 'cb88e1369aa44569a1958e745be7d769_4', '0f4d0a599b714a22a81be8c3da477a39_4', 'ce5f9c5e976746858a7c42268f48bdf9_4', 'fdd3faeaffa948dbbb557852dbccb10a_4', 'bb9ffcc1a5894733b9357fb05c2f2b1a_4', '7644d69185aa4467a35655ac7a0eb9d2_4', '965dfaece327431caa08204b615613c8_4']

    get_content()