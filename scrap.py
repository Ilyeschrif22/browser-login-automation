from seleniumbase import SB

with SB(uc=True, test=True, guest=True) as sb:
    while True:
        sb.activate_cdp_mode()
        sb.goto("https://visa.vfsglobal.com/ago/en/prt/login/")
        sb.sleep(30)
        sb.solve_captcha()
        sb.wait_for_element_absent("input[disabled]")
        sb.sleep(15)
        sb.click('button#onetrust-accept-btn-handler')
        sb.type("#email", "visasensa2@gmail.com")
        sb.type("#password", "Sensaboy333$")
        sb.sleep(20)
        sb.click('button:contains("Sign In")')
        
        sb.sleep(5)



