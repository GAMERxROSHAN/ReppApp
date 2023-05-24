from django.shortcuts import render,redirect
from .forms import NawForm
import pickle
from django.template import context

def prediction(request):
	if request.method=="POST" :
		f=open("db.model", "rb")
		model=pickle.load(f)
		f.close()
		loc=request.POST.get("loc")

		ar=request.POST.get("area")
		bd=request.POST.get("bd")
		NR=request.POST.get("nr")
		G=request.POST.get("g")
		LA=request.POST.get("la")
		Cp=request.POST.get("cp")
		Ms=request.POST.get("ms")
		Se=request.POST.get("se")
		ca=request.POST.get("ca")
		cl=request.POST.get("cl")
		inte=request.POST.get("inte")
		lg=request.POST.get("lg")
		ig=request.POST.get("ig")
		gc=request.POST.get("gc")
		jt=request.POST.get("jt")
		sp=request.POST.get("sp")
		


		if (loc=="Ambivali") or (loc=="Shahad"):
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[1,0,0,0,0,0,0,0,0,0]]
			result=model.predict(d)
			a=round(result[0]*0.00000003 ,2)
			if a>0:
				msg="The predicted price of real estate is "+str(round(result[0]*0.000003 ,2))+" Lacs Rupees."
				return render(request, "result.html", {"msg":msg})
			else:

				msg="The predicted price of real estate is "+str(round(result[0]*0.00000003 ,2))+" Crore Rupees."
				return render(request, "result.html", {"msg":msg})

		elif loc=="Andheri" :
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,1,0,0,0,0,0,0,0,0]]
			result=model.predict(d)
			msg="The predicted price of real estate is "+str(round(result[0]*0.0000001,2))+" Crore Rupees."
			return render(request, "result.html", {"msg":msg})
		elif loc=="Asangaon":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,1,0,0,0,0,0,0,0]]
			result=model.predict(d)
			a=round(result[0]*0.00000003 ,2)
			if a>0:
				msg="The predicted price of real estate is "+str(round(result[0]*0.000003 ,2))+" Lacs Rupees."
				return render(request, "result.html", {"msg":msg})
			else:

				msg="The predicted price of real estate is "+str(round(result[0]*0.00000003 ,2))+" Crore Rupees."
				return render(request, "result.html", {"msg":msg})
		elif loc=="Dombivali":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,1,0,0,0,0,0,0]]
			result=model.predict(d)
			a=round(result[0]*0.00000003 ,2)
			if a>0:
				msg="The predicted price of real estate is "+str(round(result[0]*0.000003 ,2))+" Lacs Rupees."
				return render(request, "result.html", {"msg":msg})
			else:

				msg="The predicted price of real estate is "+str(round(result[0]*0.00000003 ,2))+" Crore Rupees."
				return render(request, "result.html", {"msg":msg})
		elif loc=="Ghatkopar":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,0,1,0,0,0,0,0]]
			result=model.predict(d)
			msg="The predicted price of real estate is "+str(round(result[0]*0.0000001,2))+" Crore Rupees."
			return render(request, "result.html", {"msg":msg})
		elif loc=="Kalyan":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,0,0,1,0,0,0,0]]
			result=model.predict(d)
			a=round(result[0]*0.0000001 ,2)
			if a>0:
				msg="The predicted price of real estate is "+str(round(result[0]*0.00004 ,2))+" Lacs Rupees."
				return render(request, "result.html", {"msg":msg})
			else:
				msg="The predicted price of real estate is "+str(round(result[0]*0.0000003 ,2))+" Crore Rupees."
				return render(request, "result.html", {"msg":msg})
		elif loc=="Malad":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,0,0,0,1,0,0,0]]
			result=model.predict(d)
			msg="The predicted price of real estate is "+str(round(result[0]*0.0000001,2))+" Crore Rupees."
			return render(request, "result.html", {"msg":msg})
		elif loc=="Powai":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,0,0,0,0,1,0,0]]
			result=model.predict(d)
			msg="The predicted price of real estate is "+str(round(result[0]*0.0000001,2))+" Crore Rupees."
			return render(request, "result.html", {"msg":msg})
		elif loc=="Thane":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,0,0,0,0,0,1,0]]
			result=model.predict(d)
			msg="The predicted price of real estate is "+str(round(result[0]*0.0000001,2))+" Crore Rupees."
			return render(request, "result.html", {"msg":msg})
		elif loc=="Worli":
			d=[[ar,bd,NR,G,LA,Cp,Ms,Se,ca,cl,inte,lg,ig,gc,jt,sp]+[0,0,0,0,0,0,0,0,0,1]]
			result=model.predict(d)
			msg="The predicted price of real estate is "+str(round(result[0]*0.0000001,2))+" Crore Rupees."
			return render(request, "result.html", {"msg":msg})

		else:
			msg="The "+loc+" is not available"
			return render(request, "result.html", {"msg":msg})
		
		print(loc)
	
		fm=NawForm()
		return render(request, "prediction.html", {"fm":fm })
	else:
		msg="PLEASE GIVE REAL ESTATE DETAILS FOR A PREDICTION"
		fm=NawForm()
		return render(request, "prediction.html", {"fm":fm,"msg":msg})


def result(request):
	return render(request, "result.html")

