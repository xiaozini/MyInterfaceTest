from PageLocators.LoginLocators import LoginLocator
#登录异常用例数据
wrong_login_datas=[
    {'casename':'登录_不输入用户名','user':'','pwd':'123','loc':LoginLocator.eles[0],'expect':'用户名或密码不对','result':LoginLocator.text},
    {'casename':'登录_不输入密码','user':'nxk','pwd':'','loc':LoginLocator.eles[1],'expect':'用户名或密码不对','result':LoginLocator.text}
]