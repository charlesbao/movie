#coding=utf8
import requests

url = 'http://115.com/web/lixian/?ct=lixian&ac=add_task_url'
header = {
    'Host':'http://115.com',
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.0.0',
    'Referer':'http://115.com/?tab=offline&mode=wangpan',
}
cookies = {
    'OOFL':'361451305',
    'UID':'361451305_A1_1465287365',
    'CID':'8cbc834dbd6cb75cb0e0394b0456cb04',
    'PHPSESSID':'5hg93gt3hvobiesa4ssmlbfg40',
    'SEID':'ac2dfbc37b7e5976c713e03b34a455a7117ee4ce362bec87e218b29d3e1aae95a6b95f83d819854e7977b28f25bd8ccbad6d94d0208a132eb6ec332c',

}
data = {
    'uid':'361451305',
    'sign':'ef4a37100fc152b463d7bbbcbcd5a576a0352585',
    'time':'1465287370',
    'url':'magnet:?xt=urn:btih:00CA6F0D5EB5BFB4A72AA5BA457AF2039088B480&dn=SAYU-05&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://p4p.arenabg.ch:1337&tr=http://open.nyaatorrents.info:6544/announce&tr=udp://tracker.leechers-paradise.org:6969&tr=udp://9.rarbg.to:2710&tr=udp://eddie4.nl:6969/announce&tr=udp://9.rarbg.me:2710/announce&tr=udp://9.rarbg.com:2710/announce&tr=udp://tracker.opentrackr.org:1337&tr=udp://zer0day.ch:1337&tr=udp://tracker.sktorrent.net:6969&tr=udp://tracker.aletorrenty.pl:2710'
}
contents = requests.post(url,data = data,headers = header,cookies = cookies).content
print contents