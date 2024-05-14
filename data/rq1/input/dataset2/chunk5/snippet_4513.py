#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from appium.webdriver.common.mobileby import MobileBy

class Locators(object):    
    def setLocators(self):
        if (self.platform=='android'):
            ACEPTAR_PERMISO_BTN = (MobileBy.ID,"com.android.packageinstaller:id/permission_allow_button")
            ACEPTAR_LOGIN_BTN = (MobileBy.ID,"com.entel.movil:id/btnLogin")
            ACEPTAR_MENSAJE_ERROR_BTN = (MobileBy.ID,"com.entel.movil:id/btnPositive")
            INGRESAR_NUMERO_TXT = (MobileBy.ID,"com.entel.movil:id/etNumber")
            INGRESAR_PASSWORD_TXT = (MobileBy.ID,"com.entel.movil:id/etPassword")
        elif (self.platform=='iOS'):
            INGRESAR_PASSWORD_TXT= (MobileBy.ID,"//XCUIElementTypeSecureTextField[1]")
            ACEPTAR_LOGIN_BTN = (MobileBy.ID,"INGRESAR")