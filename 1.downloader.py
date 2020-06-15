# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import requests
import time
import concurrent.futures

# 1.找url： 有时候url中有规律，如果没有规律，就通过1.模拟访问的方式 2.找规律
# 2.把url放入容器（通过循环，字符串链接）
img_urls = ['https://images.unsplash.com/photo-1591925873173-83f5b5613e0b',
            'https://images.unsplash.com/photo-1583425423320-2386622cd2e4',
            'https://images.unsplash.com/photo-1591643529995-aef2e1e6f281',
            'https://images.unsplash.com/photo-1591868283584-abe4232655b7',
            'https://images.unsplash.com/photo-1591759092107-d55d53e2e250',
            'https://images.unsplash.com/photo-1591882351016-6f26999cea0a',
            'https://images.unsplash.com/photo-1591791077933-3b5446a113b7',
            'https://images.unsplash.com/photo-1591793217615-4581d5d05f0b',
            'https://images.unsplash.com/photo-1591777877953-786783dd25e7']

start_time = time.perf_counter()


def img_downloader(img_url):
    img_contents = requests.get(img_url).content
    # 不推荐这样print出来，会看到大量1\\\x04R\xce\xe21\xa9U\xb0\x04\rE\xae5\xf6\xeb\x
    # print(img_contents)
    # 当然，也可以通过- 作为sep
    img_name = img_url.split('/')[3]
    print(img_name)
    img_name = f'{img_name}.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(img_contents)
        print(f'{img_name}已经下载成功......')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(img_downloader, img_urls)

end_time = time.perf_counter()

print(f'整个项目下载花费了【{end_time - start_time}】秒')



# 1.I/O 密集型的项目，都可以通过多线程提升效率
# 2.一个容器把需要访问/操作的内容装起来（下载器，爬虫）
# 3.对名字进行处理——为了批量储存（注意储存类型binary/后缀）