from django.shortcuts import render
from urls.models import User
from urls.models import Urls
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def login(request):
    '''用户登录页面'''
    #post请求
    if request.method=='POST':
        #获取登录信息
        username=request.POST['username']
        passwd=request.POST['passwd']
        #检查数据
        if len(username)!=0 and len(passwd)!=0:
            #查询数据是否存在,存在则返回首页，不存在则前往注册界面
            islogin = User.objects.filter(username__exact=username, password__exact=passwd)
            if islogin:
                #在session中写入用户名
                request.session['username'] = username
                js_code='<script>'\
                        'alert("欢迎您,用户【{}】");'\
                        'window.location.href="/urlstool";'\
                        '</script>'.format(username)
                response=HttpResponse()
                response.write(js_code)
                return response
            else:
                js_code='<script>'\
                        'alert("该用户尚未注册,请先注册");'\
                        'window.location.href="/register";'\
                        '</script>'
                response=HttpResponse()
                response.write(js_code)
                return response
        else:
            js_code='<script>'\
                    'alert("用户账号与用户密码不能为空");'\
                    'window.location.href="/login";'\
                    '</script>'
            response=HttpResponse()
            response.write(js_code)
            return response
    #非post请求
    else:
        #判断是否已经登录
        if request.session.has_key('username'):
            HttpResponseRedirect('/urlstool')
        else:
            return render(request,'login.html')

def register(request):
    '''用户注册页面'''
    #post请求
    if request.method=='POST':
        #获取数据
        username=request.POST['username']
        passwd=request.POST['passwd']
        confirmpasswd=request.POST['confirmpasswd']
        #检查数据
        if len(username)!=0 and len(passwd)!=0 and len(confirmpasswd)!=0:
            #检查数据库是否已经存在注册用户
            try:
                User.objects.get(username=username)
                js_code='<script>'\
                        'alert("用户已经存在，请重新注册");'\
                        'window.location.href="/register";'\
                        '</script>'
                response=HttpResponse()
                response.write(js_code)
                return response
            except:
                #判断两次密码是否输入一致
                if passwd==confirmpasswd:
                    User.objects.get_or_create(username=username,password=passwd,isadmin=0)     #管理员0-否，1-是，默认为0，可以在后台手动修改
                    js_code='<script>'\
                            'alert("恭喜您，注册成功");'\
                            'window.location.href="/login";'\
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
                else:
                    js_code='<script>'\
                            'alert("用户密码与确认密码输入不一致，请重新注册");'\
                            'window.location.href="/register";'\
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
        else:
            js_code='<script>'\
                    'alert("用户名称、用户密码、确认密码不能为空");'\
                    'window.location.href="/register";'\
                    '</script>'
            response=HttpResponse()
            response.write(js_code)
            return response
    #非post请求
    else:
        #判断是否已经登录
        if request.session.has_key('username'):
            HttpResponseRedirect('/urlstool')
        else:
            return render(request,'register.html')

def home(request):
    '''首页'''
    #判断是否已经登录
    if request.session.has_key('username'):
        nav1=request.session['username']
        nav2='/urlstool'
        nav3='退出'
        nav4='/logout'
    else:
        nav1='注册'
        nav2='/register'
        nav3='登录'
        nav4='/login'
    return render(request,'home.html',{'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4})

def urls_all(request):
    '''所有链接列表'''
    # 判断是否已经登录
    if request.session.has_key('username'):
        nav1=request.session['username']
        nav2='/urlstool'
        nav3='退出'
        nav4='/logout'
    else:
        nav1='注册'
        nav2='/register'
        nav3='登录'
        nav4='/login'
    # 添加新链接地址信息
    if request.method=='POST':
        if request.session.has_key('username'):
            urlname=request.POST['urlname']
            urltype=request.POST['urltype']
            urltestenv=request.POST['testenv_url']
            urlformalenv=request.POST['formalenv_url']
            # 获取uid
            getuser=User.objects.filter(username=request.session['username']).values()
            getuid=list(getuser)[0]['id']
            # 检查数据
            if len(urlname)!=0 and len(urltype)!=0 and len(urltestenv)!=0 and len(urlformalenv)==0:
                try:
                    Urls.objects.create(urlname=urlname,urltype=urltype,urltestenv=urltestenv,uid=getuid)
                    js_code='<script>'\
                            'alert("链接新增成功");'\
                            'window.location.href="/urls_all";'\
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
                except:
                    js_code='<script>'\
                            'alert("链接新增失败,请重新操作");'\
                            'window.location.href="/urls_all"'\
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
            elif len(urlname)!=0 and len(urltype)!=0 and len(urlformalenv)!=0 and len(urltestenv)==0:
                try:
                    Urls.objects.create(urlname=urlname,urltype=urltype,urlformalenv=urlformalenv,uid=getuid)
                    js_code='<script>'\
                            'alert("链接新增成功");'\
                            'window.location.href="/urls_all";'\
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
                except:
                    js_code='<script>' \
                            'alert("链接新增失败,请重新操作");' \
                            'window.location.href="/urls_all"' \
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
            elif len(urlname)!=0 and len(urltype)!=0 and len(urlformalenv)!=0 and len(urltestenv)!=0:
                try:
                    Urls.objects.create(urlname=urlname,urltype=urltype,urltestenv=urltestenv,urlformalenv=urlformalenv,uid=getuid)
                    js_code='<script>'\
                            'alert("链接新增成功");'\
                            'window.location.href="/urls_all";'\
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
                except:
                    js_code='<script>' \
                            'alert("链接新增失败,请重新操作");' \
                            'window.location.href="/urls_all"' \
                            '</script>'
                    response=HttpResponse()
                    response.write(js_code)
                    return response
            else:
                js_code='<script>'\
                        'alert("链接名称、链接类型不能为空，测试链接地址与正式链接地址需要填写一个地址");'\
                        'window.location.href="/urls_all";'\
                        '</script>'
                response=HttpResponse()
                response.write(js_code)
                return response
        else:
            js_code='<script>'\
                    'alert("用户未登录，没有权限进行新增链接操作");'\
                    'window.location.href="/login";'\
                    '</script>'
            response=HttpResponse()
            response.write(js_code)
            return response
    #获取所有的链接数据
    allurls=Urls.objects.values()
    return render(request,'urls_all.html',{'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'allurls':allurls})

def logout(request):
    '''退出登录'''
    #先检查是否处于登录状态
    if request.session.has_key('username'):
        username=request.session['username']
        #删除key并重定向到首页
        del request.session['username']
        js_code='<script>'\
                'alert("当前用户【{}】退出成功");'\
                'window.location.href="/login";'\
                '</script>'.format(username)
        response=HttpResponse()
        response.write(js_code)
        return response
    else:
        HttpResponseRedirect('/login')