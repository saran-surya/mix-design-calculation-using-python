def inputs():
    #height=float(input("Height of concreting : "))                                                     
    #breadth=float(input("Breadth of conrcreting : "))
    #lenght=float(input("Length of concreting : "))
    
    
    exp_s=concretegradefin()
    print(exp_s)
    cc=conditions_wc_1(exp_s)#step 2
    target=target_s(int(cc[2]))#step 1
    water_cement_ratio=cc[1]
    min_cement=cc[0]
    cement_grade=cc[2]
    print(cc)
    workablity=workablity_1()
    aggreate_max_size=aggreatesize()#nominal aggreate size
    water_content_kg_a=w_content(aggreate_max_size,workablity)#water content
    water_content_kg=water_content_kg_a[0]
    print("water content rounded off to",water_content_kg,"kg")
    cement_content_kg=c_content(water_cement_ratio,water_content_kg)
    print("min cement required",min_cement,"\ncement grade",cement_grade,"\ncement content",cement_content_kg,"\nfck",target)
    propotion=ca_fa_prop(aggreate_max_size,water_cement_ratio)
    propotion_1=(round(propotion,2))
    ca_fa_prop_1=ca_fa_prop_2(propotion_1)
    coarseag,fineag=ca_fa_prop_1[0],ca_fa_prop_1[1]
    finaldesign=mixcalc(coarseag,fineag,cement_content_kg,water_content_kg,water_content_kg_a[1])
    print("\n\n\n")
    print("water content\t=\t",water_content_kg)
    print("\ncement content\t=\t",cement_content_kg)
    if(finaldesign[2]==1):
        print("\nadmixture content\t=\t7 kg")
    print("\nfine aggreate content\t=\t",finaldesign[1])
    print("\ncoarse aggreate content\t=\t",finaldesign[0])
    return("completed")


def workablity_1():
    x=float(input("please type your workablity,\n{if you want to exit please press'0'}\n minimum workablity is 15\nworkablity in mm : "))
    if(int(x)==0):
        import sys
        sys.exit()
    elif(x>=15.0):
        return(x)
    else:
        print("type workablity more than 15mm!!")
        return(workablity_1())

def mixcalc(ca,fa,cc,wc,con):
    cc_1=1
    sg_ce=float(input("please enter the specific gravity of cement : "))
    print(cc)
    print(wc)
    ce_1=round((cc/(sg_ce*1000)),3)
    wc_1=round((wc/1000),3)
    temm=0
    if(con==1):
        temm=0.006
    total=round(cc_1-(ce_1+wc_1+temm),3)
    print(total)
    sg_ca=float(input("please enter the specific gravity of coarse aggreate : "))
    sg_fa=float(input("please enter the specific gravity of the fine aggreate : "))
    ca_1=round((total*ca*sg_ca*1000),3)
    fa_1=round((total*fa*sg_fa*1000),3)
    return(ca_1,fa_1,con)

def ca_fa_prop_2(fp):
    coarse=fp
    fine=1-coarse
    return(coarse,fine)

def ca_fa_prop(size,water_ratio_1):# propotions
    zones=int(input("please provide the zone of coarse aggreate\n{if you want to exit please press '0'}\n1) Zone 1\n2) Zone 2\n3) zone 3\n4) zone 4\n please provide your choice as a number : "))
    zones_av=[1,2,3,4]
    if(zones==0):
        import sys
        sys.exit()
    elif(zones in zones_av):
        if(zones==1):
            z1=[0.44,0.6,0.69]
            tem=cafaprop(z1[size-1],water_ratio_1)
            return (tem+z1[size-1])
        elif(zones==2):
            z2=[0.46,0.62,0.71]
            tem=cafaprop(z2[size-1],water_ratio_1)
            return (tem+z2[size-1])
        elif(zones==3):
            z3=[0.48,0.64,0.73]
            tem=cafaprop(z3[size-1],water_ratio_1)
            return (tem+z3[size-1])
        else:
            z4=[0.5,0.66,0.75]
            tem=cafaprop(z4[size-1],water_ratio_1)
            return(tem+z4[size-1])
    else:
        return(ca_fa_prop(size,water_ratio_1))

def cafaprop(x,water_ratio_2):#propotion final
    if(water_ratio_2<0.5):
        tem1=((0.5-water_ratio_2)/(0.05))*0.01
    elif(water_ratio_2>0.5):
        tem1=((water_ratio_2-0.5)/(0.05))*0.01
    else:
        tem1=0
    
    return(tem1)

def c_content(ratio,cont):
    print(ratio)
    return(round(cont/ratio))


def w_content(x,work):
    wc=[208,186,165]
    watercont=wc[x-1]
    watercont_1=checkcontent(watercont,work)
    watercont_2=admixtures(watercont_1)
    return(watercont_2)

def admixtures(water_1):
    print("Is admixtures added to concrete")
    con=int(input("please choose from the options below\n1)yes\n2)No\nplease enter your choice as a number : "))
    if(con==1):
        print("reducing 29% of  from : ",water_1)
        water_2=(water_1)-((29/100)*water_1)
        return(round(water_2),con)
    elif(con==2):
        return (water_1,con)
    else:
        return(admixtures(water_1))

def checkcontent(y,work_1):
    if(work_1>=15 and work_1<=50):
        return(y)
    else:
        work_2=(((work_1-50)/25)*3)/100
        return(round(y+(y*work_2)))
            
def aggreatesize():
    aggreate_max_1=int(input("please choose the aggreate size from the list below as options\n{if you want to exit please press'0'}\n1)10 mm\n2)20mm\n3)40mm\n please enter your choice : "))
    con=[1,2,3]
    if(aggreate_max_1==0):
        import sys
        sys.exit()
    elif(aggreate_max_1 in con):
        return(aggreate_max_1)
    else:
        return(aggreatesize())

def concretegradefin():#input cement grade
    exp_s_1=int(input("\nplease choose the options of grade of concrete from the list below\n {if you want to exit please press'0'}\n1) M 10\n2) M 15\n3) M 20\n4) M 25\n5) M 30\n6) M 35\n7)M 40 \nplease enter your choice as a number : ")) 
    if(exp_s_1<=7 and exp_s_1 !=0):
        c_grade=[10,15,20,25,30,35,40]
        exps_1=c_grade[exp_s_1-1]
        return(exps_1)
    elif(exp_s_1==0):
        import sys
        sys.exit()
    else:
        print("\n''please choose a valid option''\n")
        return(concretegradefin())
    
def target_s(exp):#step 1
    x=exp+1.65*(deviation(exp))
    return(x)

def deviation(exp_1):# step 1_1
    if(exp_1<=15):
        return(3.5)
    elif(exp_1<=25 and exp_1>=20):
        return(4.0)
    else:
        return(5.0)

def conditions_wc_1(ex):#step2(water content)
    print("\n\nplease select the exposure conditions of the site in the given list below\n {if you want to exit please press '0'}")
    expos=int(input("\n1) Mild\n2)Moderate\n3)Severe\n4)Very Severe\n5)Extreme\nPlease enter your choice as a number : "))
    con=['1','2','3','4','5']
    
    if(expos==0):
        import sys
        sys.exit()
    elif(str(expos) in con):
        #pcc
        expos=str(expos)
        concrete_type=concrete_type_1()#get concrete type
        tem1=[]
        if(concrete_type==1):# for pcc (((needs editing)))
            min_c_1=[220,240,250,260,280]
            max_wc_1=[0.6,0.6,0.5,0.45,0.4]
            min_gr_1=[10,15,20,20,25]
            
            if(min_gr_1[con.index(expos)]>int(ex)):
                tem1.append(min_c_1[con.index(expos)])
                tem1.append(max_wc_1[min_gr_1.index(min_gr_1[con.index(expos)])])
                print(" the concrete strength is altered to : ",min_gr_1[con.index(expos)])
                tem1.append(min_gr_1[con.index(expos)])
            else:
                if(int(ex)>25):
                    cem=min_gr_1[con.index(str(expos))]
                    tem1.append(min_c_1[con.index(str(expos))])
                    tem1.append(max_wc_1[con.index(str(expos))])
                    print("the cement required for this operation is restricted to : ",cem,"\n as the use of M ",ex,"is considered to be uneconomical")
                    tem1.append(cem)
                else:
                    tem1.append(min_c_1[con.index(expos)])
                    tem1.append(max_wc_1[min_gr_1.index(int(ex))])
                    tem1.append(int(ex))

                
        else:# for rcc
            #rcc
            min_c_2=[300,300,320,340,360]
            max_wc_2=[0.55,0.5,0.45,0.45,0.4]
            min_gr_2=[20,25,30,35,40]
            
            if(min_gr_2[con.index(expos)]>int(ex)):
                tem1.append(min_c_2[con.index(str(expos))])
                tem1.append(max_wc_2[min_gr_2.index(min_gr_2[con.index(expos)])])
                print(" the concrete strength is altered to : ",min_gr_2[con.index(expos)])
                tem1.append(min_gr_2[con.index(expos)])
            else: 
                tem1.append(min_c_2[con.index(str(expos))])
                tem1.append(max_wc_2[min_gr_2.index(int(ex))])
                tem1.append(int(ex))
        return(tem1)
    else:
        conditions_wc_1(ex)
        
def concrete_type_1():
    print("\n\nplease select a valid choice from the list below as numbers\n {if you want to exit please press '0'}")
    concretety=int(input("\n select the type of concrete:\n\n1)Plain concrete\n2)Reinforced cement concrete \nPlease enter your choice as a number : "))
    con_1=['1','2']
    if(concretety==0):
        import sys
        sys.exit()
    elif(str(concretety) in con_1):
        return(int(concretety))
    else:
        return(int(concrete_type_1()))
        

print("welcome")
xxy=inputs()