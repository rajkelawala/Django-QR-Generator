import qrcode
from django.shortcuts import render
from io import BytesIO
import base64
from .forms import QRCodeForm

def generate_qr(request):
    qr_image = None
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            qr = qrcode.make(text)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_image = base64.b64encode(buffer.getvalue()).decode()

    else:
        form = QRCodeForm()

    return render(request, "index.html", {"form": form, "qr_image": qr_image})
