import os
import qrcode
from qrcode.image.styledpil import StyledPilImage

# Qr code shapes  fillShape
from qrcode.image.styles.moduledrawers import SquareModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer

# qr code color gradient
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.colormasks import SquareGradiantColorMask
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask
from qrcode.image.styles.colormasks import VerticalGradiantColorMask


class QRCodeGenerator():

    features = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=20,
    border=1
    )

    def generateQR(self,text='Hii',
        qrfillshape='Square', 
        gradient_style='Radial',
        bacground_color=(255,255,255),
        color2=(105, 66, 245),
        color1=(245, 66, 78)):

        self.features.add_data(text)
        self.features.make(fit=True)

        moduleDrawer = {
            "Square" : SquareModuleDrawer(),
            "GappedSquare": GappedSquareModuleDrawer(),
            "Circle" : CircleModuleDrawer(),
            "Round" : RoundedModuleDrawer(),
            "VerticalBars" : VerticalBarsDrawer(),
            "HorizontalBars" : HorizontalBarsDrawer()
        }

        colorMask =  {
            "Solid" : SolidFillColorMask(back_color = bacground_color, front_color = color1),
            "Radial" : RadialGradiantColorMask(back_color = bacground_color, center_color = color1, edge_color = color2),
            "Square" : SquareGradiantColorMask(back_color = bacground_color, center_color = color1, edge_color = color2),
            "Vertical" : HorizontalGradiantColorMask(back_color = bacground_color, left_color = color1, right_color = color2),
            "Horizontal" : VerticalGradiantColorMask(back_color = bacground_color, top_color = color1, bottom_color = color2)
        } 
        
        img = self.features.make_image(image_factory=StyledPilImage, module_drawer=moduleDrawer[f"{qrfillshape}"],color_mask=colorMask[f"{gradient_style}"])
        # img.save(f"{os.getcwd()}\\Auto_Attendance\\qr\\mainQR.png")
        img.save(f"{os.getcwd()}\\kivymd\\qr\\mainQR.png")



if __name__=="__main__":
    qr1 = QRCodeGenerator()

    md = ["Square","GappedSquare","Circle","Round","VerticalBars","HorizontalBars"]
    cm = ["Solid","Radial","Square","Vertical","Horizontal"]

    for i in range(len(md)):
        for j in range(len(cm)):    
                qr1.generateQR(text=f"{i} {j}",qrfillshape=md[i], gradient_style=cm[j])
    
    # i=0
    # j=0
    # qr1.generateQR(text=f"{i} {j}",qrfillshape=md[i], gradient_style=cm[j])