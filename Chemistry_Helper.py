import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
import ttkbootstrap as ttk
import math
import seaborn as sns


xz = int(input("1. GUI for Chemical Kinetics \n2. Plot the Graphs \n Enter the input : "))

if(xz == 1):    
    ### SECOND ORDER INTEGRATED RATE LAW #####################################
    def calculate_con():
        con_i = float(con_i_entry.get())
        con_f = float(con_f_entry.get())
        time = float(time4_entry.get())
    
    
        rate_constant = (1/con_i - 1/con_f) * 1/time
        rate_order_label__con.config(text=f"Rate Constant (k): {rate_constant} mol L-1 time -1 \n\n Second-order reactions involve the collision of two reactant molecules for the reaction to occur. \n Here's how to solve their rate law: \n\n 1. Identifying the Rate Law: \n The general rate law for a second-order reaction is: Rate = k [A]^2, where: \n k is the second-order rate constant (units: M^-1⋅s^-1 or L⋅mol^-1⋅s^-1). \n [A] is the concentration of the reactant (units: M or mol/L). \n\n 2. Finding the Rate at Different Concentrations: \n Substitute different values of [A] into the rate law equation to calculate the rate at those concentrations. \n The rate increases with the square of the concentration, so even small changes in concentration can significantly affect the rate. \n\n 3. Calculating Concentration at Different Times: \n Use the integrated rate equation for a second-order reaction: 1/[A]_t = kt + 1/[A]_0, where: \n [A]_t is the concentration of the reactant at time t. \n [A]_0 is the initial concentration of the reactant. \n k is the rate constant. \n t is the time elapsed. \n This equation is not linear, so solving for concentration requires specific methods like graphical or numerical techniques. ", font='Calibri 12 bold')
            
            
    ###  SECOND ORDER HALF LIFE ###########################################
            
    def calculate_second():    
        RC = float(RC_entry.get())
        conc4 = float(conc4_entry.get())
        
        half_life = 1 / (RC * conc4)
        rate_order_label_sec.config(text=f"Half-life of Second Order: {half_life} seconds \n\n 1. Apply the Integrated Rate Law for Second-Order Reactions:\n The integrated rate law for second-order reactions relates the initial concentration, rate constant, and time:\n 1/[A]_t = kt + 1/[A]_0 \n Substitute the half-life definition ([A]_t = [A]_0/2) into the equation: 1/([A]_0/2) = k(t_1/2) + 1/[A]_0 \n\n 2. Solve for the Half-Life: \n Simplify the equation: 2/[A]_0 = k(t_1/2) + 1/[A]_0 \n Multiply both sides by [A]_0: 2 = k(t_1/2)[A]_0 + 1 \n Rearrange the equation to isolate t_1/2: t_1/2 = (2 - 1/[A]_0) / k[A]_0 \n\n 3. Plug in the Values and Calculate: \n Substitute the known values of k and [A]_0 into the equation. \n Calculate the value of t_1/2, which represents the half-life of the second-order reaction. ", font='Calibri 12 bold')        
    
    ### RATE CONSTANT FOR PRESSURE  ##########################################   
    def calculate_pres():        
        p_i_ = float(p_i_entry.get())
        p_f_ = float(p_f_entry.get())
        time3 = float(time3_entry.get()) 
        thunder = math.log(p_i_ / (2*p_i_ - p_f_))
        Rate_Constant = ((math.log(10)/time3) * thunder)/2.3025
        rate_order_label__pres.config(text=f"Rate Constant: {Rate_Constant} s^-1", font='Calibri 12 bold')    
     
                    
    ### RATE OF REACTION  #################################################        
    def calculate_rate():   
        initial = float(initial_entry.get())
        final = float(final_entry.get())
        reaction_time = float(reaction_time_entry.get())
    
        rate_constant = (final - initial) / reaction_time
        rate_order_label__ror.config(text=f"Rate Constant: {rate_constant} seconds", font='Calibri 12 bold')        
    
    
    ### INTEGRATED RATE LAW FOR FIRST ORDER REACTION ###########################
    def calculate_rate_constant_f():
        final_concentration = float(final_conc2_entry.get())
        initial_concentration = float(initial_conc2_entry.get())
        time = float(time2_entry.get())
    
        rate_constant = math.log(final_concentration / initial_concentration) / time
        result_label__f.config(text=f"Rate Constant (k): {rate_constant} mol L-1 time -1 \n\n 1. Apply the Integrated Rate Law for First-Order Reactions: \n For a first-order reaction, the integrated rate law is: ln([A]) = -kt + ln([A]₀) \n k is the rate constant (s⁻¹). \n [A] is the concentration of A at time t. \n [A]₀ is the initial concentration of A. \n\n 2. Linearize the Equation: \n Take the natural logarithm (ln) of both sides of the equation: ln([A]) = -kt + ln([A]₀) \n This transforms the exponential relationship into a linear one: y = mx + c \n\n 3. Calculate the Rate Constant (k): \n From the slope (m) of the linear graph, calculate the rate constant: k = -m.\n\n Substitute the obtained value of k into the general rate law for a first-order reaction: Rate = k[A].", font='Calibri 12 bold')
    
    
    ### INTEGRATED RATE LAW FOR ZERO ORDER REACTION ##############################
    def calculate_concentration():
        initial_concentration = float(initial_concs1_entry.get())
        rate_constant = float(rate_cons1_entry.get())
        time = float(time1_entry.get())
    
        concentration = ( initial_concentration - (rate_constant * time))
        result_label__conc.config(text=f"Concentration at time {time} seconds: {concentration} mol L-1 time -1 \n \n Zero-order reactions are unique in that their rate is independent of the concentration of the reactants. Here's how to solve their rate law: \n 1. Identifying the Rate Law: \n The rate law for a zero-order reaction is simply: Rate = k, where k is the rate constant. \n The rate constant has units of concentration per time (e.g., M/s, mol/L⋅s). \n\n 2. Finding the Rate at Different Concentrations: \n Since the rate is independent of concentration, it remains the same regardless of the initial reactant concentration. \n To find the rate at any concentration, simply substitute the value of the rate constant (k) into the rate law equation. \n\n 3. Calculating Concentration at Different Times:\n Use the integrated rate equation for a zero-order reaction: [A]_t = [A]_0 - kt, where:\n [A]_t is the concentration of the reactant at time t.\n [A]_0 is the initial concentration of the reactant.\n k is the rate constant.\n t is the time elapsed.\n\n 4. Interpreting the Rate Law\n The fact that the rate is independent of concentration indicates that the rate-determining step in the reaction does not involve the reactants directly.\n This could be due to factors like a slow surface reaction or a constant supply of reactants.", font='Calibri 12 bold')
    
    ### FIRST ORDER HALF LIFE #############################################
     
    def calculate_first_life():    
        rate_constant = float(rate_constant_entry_1.get())
        
        half_life = (0.693) / (rate_constant)
        result_label_first.config(text=f"Half-life: {half_life} seconds \n \n In first-order reactions, the rate of reaction is directly proportional to the remaining concentration of the reactant.\n Here's how to solve for the half-life (t_½) of a first-order reaction: \n\n Using the Half-Life Formula: \n Formula: t_½ = 0.693 / k \n Steps: \n Identify the rate constant (k) of the reaction. It is usually given in units of s^(-1) or min^(-1).\n Substitute the value of k into the formula. \n Calculate the half-life.", font='Calibri 12 bold')  
     
    ### ZERO ORDER HALF LIFE #############################################
    def calculate_half_life():    
        initial_concentration = float(initial_conc_ze_entry.get())
        rate_constant = float(rate_const_ze_entry.get())
        
        half_life = initial_concentration / (2 * rate_constant)
        result_label_ze.config(text=f"Half-life: {half_life} seconds", font='Calibri 12 bold') 
     
     
     
    ### ARRHENIUS EQUATION  #################################################    
    def calculate_rate_constant():        
        activation_energy = float(activation_entry.get())
        pre_exponential_factor = float(pre_exponential_entry.get())
        temperature = float(temp_entry.get())  # Convert Celsius to Kelvin
        gas_constant = 8.314  # J/(mol*K)
        
        rate_constant = pre_exponential_factor * (2.71828 ** (-activation_energy / (gas_constant * (temperature + 273.15))))
        result_label__ar.config(text=f"Rate Constant: {rate_constant}  mol L-1 time -1 \n\n The Arrhenius equation relates the rate constant (k) of a chemical reaction to temperature (T) and activation energy (Ea).\n Here's how to solve it for different variables: \n\n 1. Finding k (rate constant) at a given temperature: \n Given: Ea, T, and A (pre-exponential factor) \n Steps: \n Convert temperature to Kelvin (T in K). \n Substitute all values in the equation: k = A * exp(-Ea/RT) \n Calculate the natural exponent using a calculator. \n Multiply the result by A to get the final k value. \n\n 2. Finding Ea (activation energy) at a known k and T: \n Given: k, T, and A \n Steps: \n Take the natural logarithm of both sides of the equation: ln(k) = ln(A) - Ea/RT \n Rearrange the equation to isolate Ea: Ea = -RT * ln(k/A) \n Substitute all values and calculate Ea. Ensure consistent units (mostly Joules/mol).", font='Calibri 12 bold')    
            
            
    # for windows title 
    window = ttk.Window(themename = 'darkly')
    window.title("Chemistry Helper")
    
    # for geometry types in application
    window.geometry("620x450+350+100")
    
    # TABS and NOTEBOOK
    notebook = ttk.Notebook(window)
    
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    tab4 = ttk.Frame(notebook)
    tab5 = ttk.Frame(notebook)
    tab6 = ttk.Frame(notebook)
    tab7 = ttk.Frame(notebook)
    tab8 = ttk.Frame(notebook)
    tab9 = ttk.Frame(notebook)
    tab10 = ttk.Frame(notebook)
    
    notebook.add(tab1, text='Index')
    notebook.add(tab2, text='Arr. Eq.')
    notebook.add(tab3, text='H.L 1st')
    notebook.add(tab4, text='R.L 0')
    notebook.add(tab5, text='R.L 2nd ')
    notebook.add(tab6, text='H.L 2nd')
    notebook.add(tab7, text='R.L 1st')
    notebook.add(tab8, text='R.C for P.')
    notebook.add(tab9, text='H.L 0')
    notebook.add(tab10, text='R.C')
    
    
    ### TAB 1  ################################
    
    label = ttk.Label(tab1, text='CHEMICAL KINETICS HELPER', font= 'Calibri 30 bold')
    label.pack()
    
    label = ttk.Label(tab1, text="\nSelect The Type of Operation You Want To Perform", font='Calibri 15 bold')
    label.pack()
    
    item = ('SECOND ORDER RATE LAW','SECOND ORDER -> Half Life', 'FIRST ORDER -> INTEGRATED RATE LAW', 'ARRHENIUS EQUATION','ZERO ORDER -> Half Life','REACTION RATE','Rate Constant With Pressure','FIRST ORDER -> Half Life','ZERO ORDER -> INTEGRATED RATE LAW' )
    cal = tk.StringVar(value = item[0])
    combo = ttk.Combobox(tab1, textvariable=cal , value= item)
    combo['value'] = item
    combo.pack()
    
    ### TAB 2  ###############################
    
    label = ttk.Label(tab5, text='SECOND ORDER RATE LAW -> Rate Constant = (1/Initial Concentratioin - 1/Final Concentratioin) * 1/time', font='Calibri 10 bold')
    label.pack()
    
    con_i = ttk.Label(tab5, text=" Initial Concentration in mol/m^3 ")
    con_i.pack(pady=10)
    con_i_entry = ttk.Entry(tab5)
    con_i_entry.pack(pady=10)
    
    con_f = ttk.Label(tab5, text=" Final Concentration in mol/m^3 ")
    con_f.pack(pady=10)
    con_f_entry = ttk.Entry(tab5)
    con_f_entry.pack(pady=10)
    
    time4 = ttk.Label(tab5, text=" Time in s ")
    time4.pack(pady=10)
    time4_entry = ttk.Entry(tab5)
    time4_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab5, text="Calculate", command=calculate_con)
    calculate_button.pack(pady=10)
    
    
    rate_order_label__con = ttk.Label(tab5, text="")
    rate_order_label__con.pack()
    
    ### TAB 3  ###############################
    
    label = ttk.Label(tab6, text='SECOND ORDER -> Half Life -> 1/Rate constant*Concentration', font='Calibri 12 bold')
    label.pack()
    
    RC = ttk.Label(tab6, text=" Rate Constant in mol/L s")
    RC.pack(pady=10)
    RC_entry = ttk.Entry(tab6)
    RC_entry.pack(pady=10)
    
    conc4 = ttk.Label(tab6, text=" Concentration in mol/m^3 ")
    conc4.pack(pady=10)
    conc4_entry = ttk.Entry(tab6)
    conc4_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab6, text="Calculate", command=calculate_second)
    calculate_button.pack(pady=10)
    
    rate_order_label_sec = ttk.Label(tab6, text="")
    rate_order_label_sec.pack()
    
    
    ### TAB 4  ############################################
    
    label = ttk.Label(tab10, text='Rate Constant = (2.303/Time)*log(Initial pressure/(2*Initial pressure - Final Pressure)) ', font='Calibri 12 bold')
    label.pack()
    
    p_i = ttk.Label(tab10, text=" Initial pressure in pascal ")
    p_i.pack(pady=10)
    p_i_entry = ttk.Entry(tab10)
    p_i_entry.pack(pady=10)
    
    p_f = ttk.Label(tab10, text=" Final Pressure in pascal ")
    p_f.pack(pady=10)
    p_f_entry = ttk.Entry(tab10)
    p_f_entry.pack(pady=10)
    
    time3 = ttk.Label(tab10, text=" Time in s ")
    time3.pack(pady=10)
    time3_entry = ttk.Entry(tab10)
    time3_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab10, text="Calculate", command=calculate_pres)
    calculate_button.pack(pady=10)
    
    rate_order_label__pres = ttk.Label(tab10, text="")
    rate_order_label__pres.pack()
    
    
    ### TAB 5   ##################################################
    
    label = ttk.Label(tab8, text='Rate Constant = (Final Conc - Initial Conc) / Reaction Time', font='Calibri 15 bold')
    label.pack()
    
    initial = ttk.Label(tab8, text="Initial Concentration of Reaction:")
    initial.pack(pady=10)
    initial_entry = ttk.Entry(tab8)
    initial_entry.pack(pady=10)
    
    final = ttk.Label(tab8, text="Final Concentration of Reaction:")
    final.pack(pady=10)
    final_entry = ttk.Entry(tab8)
    final_entry.pack(pady=10)
    
    reaction_time = ttk.Label(tab8, text="Reaction Time (s):")
    reaction_time.pack(pady=10)
    reaction_time_entry = ttk.Entry(tab8)
    reaction_time_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab8, text="Calculate", command=calculate_rate)
    calculate_button.pack(pady=10)
    
    rate_order_label__ror = ttk.Label(tab8, text="")
    rate_order_label__ror.pack()
    
    
    ### TAB 6   ##################################################
    
    label = ttk.Label(tab3, text='FIRST ORDER -> Half Life = Log(2) / Rate Constant', font='Calibri 12 bold')
    label.pack()
    
    rate_constant_label = ttk.Label(tab3, text="Rate Constant (k):")
    rate_constant_label.pack(pady=10)
    
    rate_constant_entry_1 = ttk.Entry(tab3)
    rate_constant_entry_1.pack(pady=10)
    
    calculate_button = ttk.Button(tab3, text="Calculate Half-life", command=calculate_first_life)
    calculate_button.pack(pady=20)
    
    result_label_first = ttk.Label(tab3, text="")
    result_label_first.pack()
    
    ### TAB 7   ##################################################
    
    label = ttk.Label(tab7, text='FIRST ORDER -> INTEGRATED RATE LAW = log(Final Concentration / Initial Concentration) / Time', font='Calibri 11 bold')
    label.pack()
    
    initial_conc2_label = ttk.Label(tab7, text="Initial Concentration ([A]₀):")
    initial_conc2_label.pack(pady=10)
    
    initial_conc2_entry = ttk.Entry(tab7)
    initial_conc2_entry.pack(pady=10)
    
    final_conc2_label = ttk.Label(tab7, text="Final Concentration ([A]):")
    final_conc2_label.pack(pady=10)
    
    final_conc2_entry = ttk.Entry(tab7)
    final_conc2_entry.pack(pady=10)
    
    time2_label = ttk.Label(tab7, text="Time (seconds):")
    time2_label.pack(pady=10)
    
    time2_entry = ttk.Entry(tab7)
    time2_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab7, text="Calculate Rate Constant", command=calculate_rate_constant_f)
    calculate_button.pack(pady=20)
    
    result_label__f = ttk.Label(tab7, text="")
    result_label__f.pack()
    
    
    ### TAB 8   ##################################################
    
    label = ttk.Label(tab4, text='ZERO ORDER -> INTEGRATED RATE LAW -> Concentration = Initial Concentration - Rate Constant * Time', font='Calibri 10 bold')
    label.pack()
    
    initial_concs1_ = ttk.Label(tab4, text="Initial Concentration ([A]₀):")
    initial_concs1_.pack(pady=10)
    
    initial_concs1_entry = ttk.Entry(tab4)
    initial_concs1_entry.pack(pady=10)
    
    rate_cons1_label = ttk.Label(tab4, text="Rate Constant (k):")
    rate_cons1_label.pack(pady=10)
    
    rate_cons1_entry = ttk.Entry(tab4)
    rate_cons1_entry.pack(pady=10)
    
    time1_label = ttk.Label(tab4, text="Time (seconds):")
    time1_label.pack(pady=10)
    
    time1_entry = ttk.Entry(tab4)
    time1_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab4, text="Calculate Concentration", command=calculate_concentration)
    calculate_button.pack(pady=20)
    
    result_label__conc = ttk.Label(tab4, text="")
    result_label__conc.pack()
    
    
    ### TAB 9   ##################################################
    
    
    label = ttk.Label(tab9, text='ZERO ORDER -> Half Life = Initial Concentration / (2 * Rate Constant)', font='Calibri 15 bold')
    label.pack()
    
    initial_conc_ze_label = ttk.Label(tab9, text="Initial Concentration ([A]₀):")
    initial_conc_ze_label.pack(pady=10)
    
    initial_conc_ze_entry = ttk.Entry(tab9)
    initial_conc_ze_entry.pack(pady=10)
    
    rate_const_ze_label = ttk.Label(tab9, text="Rate Constant (k):")
    rate_const_ze_label.pack(pady=10)
    
    rate_const_ze_entry = ttk.Entry(tab9)
    rate_const_ze_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab9, text="Calculate Half-life", command=calculate_half_life)
    calculate_button.pack(pady=20)
    
    
    result_label_ze = ttk.Label(tab9, text="")
    result_label_ze.pack()
    
    
    ### TAB 10   ##################################################
    
    label = ttk.Label(tab2, text='Arrhenius equation', font='Calibri 20 bold')
    label.pack()
    
    activation_energy = ttk.Label(tab2, text="Activation Energy (J/mol):")
    activation_energy.pack(pady=10)
    
    activation_entry = ttk.Entry(tab2)
    activation_entry.pack(pady=10)
    
    pre_exponential_factor = ttk.Label(tab2, text="Pre-exponential Factor (s^-1):")
    pre_exponential_factor.pack(pady=10)
    
    pre_exponential_entry = ttk.Entry(tab2)
    pre_exponential_entry.pack(pady=10)
    
    temperature = ttk.Label(tab2, text="Temperature (°C):")
    temperature.pack(pady=10)
    
    temp_entry = ttk.Entry(tab2)
    temp_entry.pack(pady=10)
    
    calculate_button = ttk.Button(tab2, text="Calculate", command=calculate_rate_constant)
    calculate_button.pack(pady=20)
    
    result_label__ar = ttk.Label(tab2, text="")
    result_label__ar.pack()
    
    
    notebook.pack()
    
    # end for application code
    
    window.mainloop()
else:
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    
    
    num = int(input(" 1. Arrhenius equation \n 2. Rate Law for 2nd Order \n 3. Rate law for 0th Order \n 4. Rate law for 1st Order \n 0. Exit() \n\n Enter the Input :-> "))
    
    
    if (num == 1):  
        # Function to plot Arrhenius equation
        def arrhenius_equation(pre_exponential_factor, activation_energy, temps, boltzmann_constant=8.314):
            # Convert temperatures to Kelvin if needed
            temps_kelvin = np.where(temps < 300, temps + 273.15, temps)
        
            # Calculate rate constants
            rate_constants = pre_exponential_factor * np.exp(-activation_energy / (boltzmann_constant * temps_kelvin))
        
            # Create Seaborn plot
            sns.set(style="darkgrid")
            plt.figure(figsize=(8, 6))
            plt.semilogy(temps_kelvin, rate_constants, label=f'Ea = {activation_energy:.2f} kJ/mol')
            plt.title('Arrhenius Equation')
            plt.xlabel('Temperature (K)')
            plt.ylabel('Rate Constant')
            plt.legend()
            plt.grid(True)
            plt.show()
        
        # Get input parameters from the user
        pre_exponential_factor = float(input("Enter Pre-exponential Factor: "))
        activation_energy = float(input("Enter Activation Energy (kJ/mol): "))
        min_temp = float(input("Enter Minimum Temperature: "))
        max_temp = float(input("Enter Maximum Temperature: "))
        
        # Generate temperature range
        temps = np.linspace(min_temp, max_temp, 1000)
        
        # Plot the Arrhenius equation
        arrhenius_equation(pre_exponential_factor, activation_energy, temps)
        
    
    elif(num == 2):
        # Function to plot second-order reaction
        def second_order_reaction(rate_constant, initial_concentration, max_time):
            # Generate time points
            time_points = np.linspace(0, max_time, 1000)
        
            # Calculate concentration using second-order rate law
            concentration = 1 / (1 / initial_concentration + rate_constant * time_points)
        
            # Create Seaborn plot
            sns.set(style="whitegrid")
            plt.figure(figsize=(8, 6))
            plt.plot(time_points, concentration, label=f'Rate Constant = {rate_constant}')
            plt.title('Second-Order Reaction')
            plt.xlabel('Time')
            plt.ylabel('Concentration')
            plt.legend()
            plt.show()
        
        # Get input parameters from the user
        rate_constant = float(input("Enter Rate Constant: "))
        initial_concentration = float(input("Enter Initial Concentration: "))
        max_time = float(input("Enter Maximum Time: "))
        
        # Plot the second-order reaction
        second_order_reaction(rate_constant, initial_concentration, max_time)
        
    
    elif (num == 3):
        # Function to plot zero-order reaction
        def zero_order_reaction(rate_constant, initial_concentration, max_time):
            # Generate time points
            time_points = np.linspace(0, max_time, 1000)
        
            # Calculate concentration using zero-order rate law
            concentration = initial_concentration - rate_constant * time_points
        
            # Create Seaborn plot
            sns.set(style="darkgrid")
            plt.figure(figsize=(8, 6))
            plt.plot(time_points, concentration, label=f'Rate Constant = {rate_constant}')
            plt.axhline(y=initial_concentration, color='red', linestyle='--', label=f'Initial Concentration = {initial_concentration}')
            plt.title('Zero-Order Reaction')
            plt.xlabel('Time')
            plt.ylabel('Concentration')
            plt.legend()
            plt.show()
        
        # Get input parameters from the user
        rate_constant = float(input("Enter Rate Constant: "))
        initial_concentration = float(input("Enter Initial Concentration: "))
        max_time = float(input("Enter Maximum Time: "))
        
        # Plot the zero-order reaction
        zero_order_reaction(rate_constant, initial_concentration, max_time)
            
    
    elif (num == 4):
        # Function to plot first-order half-life vs rate constant
        def plot_1st_order_half_life_vs_rate_constant(min_rate_constant, max_rate_constant):
        # Generate rate constant range
            rate_constants = np.linspace(min_rate_constant, max_rate_constant, 1000)
    
            # Calculate half-life for each rate constant
            half_lives = np.log(2) / rate_constants
    
            # Create plot
            plt.figure(figsize=(8, 6))
            plt.plot(rate_constants, half_lives, label='Half-life')
            plt.title('First-Order Half-Life vs. Rate Constant')
            plt.xlabel('Rate Constant (s^-1)')
            plt.ylabel('Half-Life (s)')
            plt.legend()
            plt.grid(True)
            plt.show()
        
            # Get input parameters from the user
        min_rate_constant = float(input("Enter Minimum Rate Constant: "))
        max_rate_constant = float(input("Enter Maximum Rate Constant: "))
        
        # Plot first-order half-life vs. rate constant
        plot_1st_order_half_life_vs_rate_constant(min_rate_constant, max_rate_constant)