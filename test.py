import os
import time
from socket import AF_INET, SOCK_STREAM, socket

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

os.chdir('Answers')


#TASK 1

inOut = [
    ('python 1.py http://www.chinatoday.com.cn/ctenglish/2018/et/202411/t20241104_800382564.html', '310\n'),
    ('python 1.py https://www.apachefriends.org/blog/new_xampp_20231119.html', '62\n'),
    ('python 1.py https://jassemrl.github.io', '77\n'),
]

passed = 0
for i,o in inOut:
    with os.popen(i) as process:
        if o == process.read():
            passed += 1

print(f'TASK 1: {passed}/{len(inOut)}')




# TASK 2
inOut = [
    (['0'], '0'),
    (['0', '0'], '00'),
    (['hell0'], '0'),
    (['Hell0', 'Pe0ple 0f the W0rld'], '0000')
]

passed=0
for i,o in inOut:
    with os.popen("python 2.py") as proc:
        print('starting')
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect(('127.0.0.1', 8080))
                s.setblocking(False)
                print('success')
                for inp in i:
                    s.sendall(inp.encode())
                time.sleep(0.1)
                o1 = s.recv(1024).decode()
                if o1 == o:
                    passed += 1
            except:
                pass
    try:
        _ = proc.read()
    except:
        pass


print(f'TASK 2: {passed}/{len(inOut)}')


# TASK 3
inp = [
    [('Hello', 0), (None, 1)],
    [('Hi', 1), (None, 0)],
    [('Hello', 0), (None, 1), ('How are you?', 1), (None, 0)],
    [('Hello', 0), ('Hi, ', 1), (None, 1), ('How are you?', 1), (None, 0)],
]

passed=0
for i in inp:
    with os.popen("python 3.py") as proc:
        with socket(AF_INET, SOCK_STREAM) as s1:         
            with socket(AF_INET, SOCK_STREAM) as s2:
                try:
                    s1.connect(('127.0.0.1', 8080))
                    s2.connect(('127.0.0.1', 8080))
                    s1.setblocking(False)
                    s2.setblocking(False)
                    scks = [s1, s2]
                    toRead = ["", ""]
                    
                    temp = True

                    for action,sockNo in i:
                        if action == None:
                            time.sleep(0.1)
                            dt = scks[sockNo].recv(1024)
                            dt = dt.decode()
                            if not toRead[sockNo] == dt:
                                temp = False
                                break
                        else:
                            scks[sockNo].sendall(action.encode())
                            toRead[(sockNo+1)%2] += action
                    
                    if temp:
                        passed += 1
                except:
                    pass
        
    try:
        _ = proc.read()
    except:
        pass

print(f'TASK 3: {passed}/{len(inOut)}')


# TASK 4

inOut = [
("Hello", "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"),
('4b3faaf4429caf6183e97590213f0c155253e0c7755edde47b565bd8e980dbf167229374614139266eceda542250cfef97c415452a168dc5888dec26531f8895403b3a76b1ba5080f1f00bd587538341746f021de63a7c3f1425b62fa6c40bf86eb1b03111213668a67e0769af777b9c61be98dd95e61cd23369fb8e1e79647a5f491f0d467cfc17ac72265389a2de9c9c66f428262106ac1918ef4e066deb926b46e71c8613acf772803f19603e1ef6e62d480d0a452a6f730e64fae491f8a745a6a1847fdc6bce1ee397457f2a2f6fa6ff43d0f5cd0ed59e0a1e3f095e955855ee73a5ef51f804a0d64428417be4aa79a8b69b39fe514b6795d2cec3ae8757', '946d8e82e637672aa7d29f59ee8ac661559a30b589ae7ee4e254f0df21e3f007'),
('3739e9e1cb10c6a9b9cc58559551edcc0ebced93b84fddeee289ac43cf96f5018125b92130b003a847499c114705b65592ac69e925318169881b8b9dad843a2336716e824a26e7ae2d4aac52bfa62bfe4a96842ccfe9dffeb6797a90340733f00b32f6be5776016dc9f199038f979155d7e7429f855e0fb6881caa30f4b060c352e020363ab52893d9427a9b9ff9752b93257e58fb300174a702317942932b3fd0e194a7d0bc10bd64f0d244047187219a2da219babed854815f433bd17401bdd6323b0b2a89b05c3b499cb6f8daaadbcd69b25a7e356f8b52acff6a60dfe2d7edb91ecfac58106aea3479f9baa80d18fe3952f9d20fd18d83792c7f496b2da0', 'c60e785e16ea9d949fd396e55417bf8098afbb355681df0cf938f97e42e42956'),
('1065d04f045549f0ea33f978281cf25284b093ea7aa83cee7b0839e2754c09b9345a4270b00822212ce4fee9ff86a2f7f86d5e38613e78b2622b66b15464180325855779e39d6ba64c921bf8df59d72086e18f1859c09d2c66a50c377bdcb3a6efc2dd54aed99d5d768aa7ff58a0c92d4060b262908c809f7a4cfb380f6a190b97367ce538de7d5952daea930798e324a50368ca8c75688473803bd01f3b78b8d2fcc14241fabfaf16eca89bff3dbd07c3a115e24c095a1a4c86cdf5c161b6953b15e1a8017c85c4cb55e06b34c790485658d3b77c47e9ad04eacdad4a56bc38f65e1c2c1b3e08aca770e716ceb35af597dfb450a9317d1c8a63b785cc1cd1b1', '014eefad881d1d09a28336c6a094f6e909033c9bae29786b32e733e8e827a975'),
('75cb4cda14b7befe77f0239a3014f8c283182ac82b4a57ba0fd3ccbe843e449661a8d9564cf71de728c613694ee50d7574cc54b5f0d356f9a931398f1f13e69eefe8d73b58b7fcfabdcadbce472c0a98c4564bafafdbfea01ab4a77042fcae04c485dfa9baae0699d76e34096548c9a22951eee089c5e8f71374c8a813418118ee635248ea071a40ffbb89b2ece4e37df90e14df0293b1bfd700cab6a83c6db7f323565e606e16e267bef115a72b0e1927230a716febfaa0d1c53ebdd3be7c944696bef75def3bd287554d72bd03966be947e27e5eb2ada132ecf626c28e0f4c54d1484075e750508f42c9ee9659696e3d7679ef3e1db6fbf894cdde163aa16d5738fa2c58fefa3e65a914430c89f851b5cf9d9468b1193ece0d2e21aeda16a7f7aa5bd0151d5268d4796668cc3a34216dd6fdd88b632d7815b4f3d87de69c2b0db4661b8a7de52548615388a9b754d226a7843fa32312c91d52e1ee2c0ce71d45a1dc564d140288b7dbf2e995fcab76b2203f76fe5d0004ad2b653286144c2649a9db30d0a186c5ed47738de9a3ebf4cc803d8a55cfa0a2e2aa78ef7ef7666c245aa03dc441cc2fa4dd0db889d3d7288515b91e0701e284e3e246f2a0c83161a8e0673c0518214b6ab8858b1ab1bce48ba980f14e9025ac05e7d5e33101334e406206307b8ef2e89ffbd22775dbc9eb6cd7386f168ba7190b900f9b3ae43a8e2efb963ec67b4bc373e4444c18f7ea33f7af7f6043e49ebeaca4c597e741a9ea33fd979c5ba4f97da7f98f5e0aa0772526d50934a5a27f297081eafc7ec0ceac4ddf6d8dbcaf9966b1a1d55667d05685ce42710f169d9b895c04226e4c91ac0dff295cc2c8ec2de0513017e29457211f787d93458e19dd087b328c5432e572e26e1bf6834cbd1e051ea61c2eab4a63256272dad2832329021b9ca28013c9f950f5f0d0ee30cd9bfb9621e5cbd204924e02be822c3f2d77705ff867a289bfccf3df36f72c1b426fc7eb526195c6ff8e29bd403f7744a69bf783942f50fe348ff7e2ad4197b96516503d72e977e50944b41fc1e3c44bb985fac0060ac2b1060f3a78359fd79f766d417b881327b80e9ad455394c26fde3ea9da8eed09c552244d9fbb1bff7a67090373e29dc0ba5b8307a327961beae586649b1263f3b553fd4d698bb31c1e8993055d93b3039ff4658bcc9de77c847c6dbdc807966cb4d2ca59e0c3e3627ebe87031a3062881a5ab9467520d12302c225c67126edc9047726c3516b9b6c55a3350e65ac4e0b1523e165c7916e6e7a2d359b6996c117f3f9dd64e0cf4e44286f11bf6a325ee03e6ff129290f5e53132e8d0e6b5b3331682cc33d14c4d1ed7dbc8f7c4dce85cea580cd5495522acb35823ac72e4d9db2d255649459e33a8f998819d038986ff74447ef33b21e16833fefe0472601c68eda574e38c84524b6bacd385bf6aad637c47a999b3798bf37bbe2beee9c0af550d219d71f49ea79d34507557a7623da8b0c9c4be032d8cf3305702c702f7a4f029264177b799f01eae5a89ed550b1cd9aff51576580ce5e7a8b3900d867eb5202ea736003e0654e0381d11a1050801f73f6c942459a36c0222210864062880902f938647a1db7ccd82196d0f250ba33aba9677238895123af98246049fcf5faa1438f30cdfe268d9506a4fc709559a2716935ed48ed88926fb9b50097aa8b0f68e0aee6d2d45d13618867906be3e9859b3e0e2725cd3a77be4a2c883b336bd686f29bc1ca8ea6785c5bc14936c567259ec1413b8400b7ce2129b2f9a2f194974a242da50876d3df40ba3be714d99a0556f40f216d306158f1187f648b0997e618e7313a50bf5c6cef9e63d900565215fa5f3a91e48307e43f13e87cb1f83d7fbd3ddc3f5bbbd4b6ea947d7aee392c216d70ab00287c8b31bc61885784e1f0513c4863973cd347207f260519ac336c50ee1b26a119fe33ddbcd6d081cc5d187a634b9c23acd9d7cfac4bebb1fd28d401c565f87308e8f0b22c8ab5c161dda8e405cb8f6cbdcd4ad1aff5227d088d16802fac2661ddfbad939d6558ea944a388a92858a9c3afe0471e87945c2dc73e95e9d554ef0b35e260193a5e56bb0fb92e9c941213bf7d9292683691663b16f4543bc2897e7588530a8d6445af531743e4a1678570d004283262b92b24b83e489620c8ea0e69d65e718dfd90158510a970ef932f1e2d8c66cf257104c3dee2b3d83743467473b44235f580a89d56780a494d2f97bf68fb23c579bdd2a8e8c783378e517c2d013fcb70fbb57474f6e5bd97d613dea93e66a8fe6a893e66c0ff8212f7375f358cf368e134c3b00fc58cc2505e36e0dac6e5f8d6efc6d540af5228f6a0d3d3f6961d7685ffc35fd7161ecb946982f142259d73c309a8f27b7deb575aadb961750e79346b31404b9fda8e6ed6f85e1d863bf20f559683cd41d5fe39c28760698ca17968b4913ac4b99c14faa0724acc37e4d1c5972b391a60bd4b31ddf4dd78696756d4d1390f7a692a85099a466460df61a6745777a21dc28598fa98547f277e3f686e5df2851715028de3e6986f78dec3eaa5765a15f6ea63c86be4c06e20e25b8f93a36908d4b528d21957c6acb68b6b181cb41854af4db692f1c8817dce4056193ce027d482fe46539c01980cf9059ca89d2261ccdeee6e1daf3eaf874ce0ac0a75a1aafd2e98b58daf1569f663aa9ea0e545a2247a1fd0a319595eb8482632cce79ac5ddac1cef356bd057b67915e20c6aea394b55ed618f0ae22f5b07d2d16b8ab6e4144ea99aabfcbb08fe324f16fba1ff4d67ffb40fbd76e7684ddf30efeb562cc2aef6003d6fc7d3d8dffac9c772ac9e35ef371f6368b60c13d40b9044c589c07ad0f2b1c86786cd4bc53acb1b6f',
 '3d70b2eb8e78ae743c88a533d251ea41ddf57b984285a5e8b370bae35bd9373d')
]


passed=0
for i,o in inOut:
    with os.popen("python 4.py") as proc:
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect(('127.0.0.1', 8080))
                s.setblocking(False)
                s.sendall(i.encode())
                time.sleep(0.1)
                o1 = s.recv(1024).decode()
                if o1 == o:
                    passed += 1
            except:
                pass
    try:
        _ = proc.read()
    except:
        pass


print(f'TASK 4: {passed}/{len(inOut)}')
