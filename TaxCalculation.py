income = int(input("Please enter your income"))

def personalAllowance(annualSalary):
    global t_s
    if(annualSalary<100000):
        print("Your personal allowance is £11,500")
        if(11500>income):
          print("You will pay no tax")
        elif(11500<income):
          print("You will pay tax")
          t_s = income - 11500
    elif(annualSalary>=100000):
        default_allowance = 11500
        total_allowance = annualSalary - 100000
        if(total_allowance%2==0):
            total_all2 = total_allowance / 2
            total_finish = default_allowance - total_all2
            print("You will recieve ",total_finish)
            t_s = income - total_finish
        else:
            print("Your value is not divisible by 2")
personalAllowance(income)

def incomeTax(e_s):
  if e_s<=32000:
    p_s = e_s * 0.2
    print("You will pay 20% tax = £", float(p_s))
    if e_s>32000 and e_s<=150000:
      p_s = e_s *0.2
      a_s = e_s * 0.4
      p_s_t = p_s + a_s
      print("You will pay 20% + 40% tax = £", float(p_s_t))
      if e_s>32000 and e_s>150000:
        p_s = e_s *0.2
        a_s = e_s * 0.4
        aa_s = e_s * 0.45
        p_s_t = p_s + a_s + aa_s
        print("You will pay 20% + 40% + 45% tax = £", float(p_s_t))
incomeTax(t_s)