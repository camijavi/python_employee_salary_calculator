from components import clearConsole, printError, printSucess, printWarning


def readEmployeeData():
    while True:
        employeeData = input("Nombre del colaborador: ").strip()
        if not employeeData:
            printError("El nombre no puede estar vacío.")
            continue
        break

    while True:
        try:
            grossSalary = float(input("Salario básico: "))
            if grossSalary < 0:
                printError("El salario no puede ser negativo.")
                continue
            break
        except ValueError:
            printError("Debe ingresar un valor numérico válido.")

    return employeeData, grossSalary


def calculateBasicDeduction(grossSalary, baseDeductionPercentage):
    return grossSalary * baseDeductionPercentage


def calculateInssDeduction(grossSalary, InssDeductionPercentage):
    return grossSalary * InssDeductionPercentage


def calculateEmploymentIncomeTax(grossSalary, InssDeductionPercentage):
    # Annualize salary and deduct the 7% INSS labor contribution.
    annualGross = grossSalary * 12
    annualInss = annualGross * InssDeductionPercentage
    annualTaxableIncome = annualGross - annualInss

    # Calculate annual IR using the progressive tax brackets.
    match annualTaxableIncome:
        case income if income <= 100000:
            annualIr = 0
        case income if income <= 200000:
            annualIr = (income - 100000) * 0.15
        case income if income <= 350000:
            annualIr = 15000 + (income - 200000) * 0.20
        case income if income <= 500000:
            annualIr = 45000 + (income - 350000) * 0.25
        case income:
            annualIr = 82500 + (income - 500000) * 0.30

    return annualIr / 12


def calculateNetSalary(grossSalary, totalDeductions):
    netSalary = grossSalary - totalDeductions
    return netSalary


def calculateNIO_USD(netSalary):
    exchangeRateNIO = 36.76
    salaryUSD = netSalary / exchangeRateNIO
    return salaryUSD


def showEmployeeNetSalary(employeeName, grossSalary, basicDeduction, inssDeduction, irDeduction, totalDeductions, netSalaryNIO, netSalaryUSD):
    basicPercentage = (basicDeduction / grossSalary * 100) if grossSalary > 0 else 0
    inssPercentage = (inssDeduction / grossSalary * 100) if grossSalary > 0 else 0
    irPercentage = (irDeduction / grossSalary * 100) if grossSalary > 0 else 0
    totalDeductionPercentage = (totalDeductions / grossSalary * 100) if grossSalary > 0 else 0

    print("\n----------------------------------------")
    print(f"Nombre del colaborador: {employeeName}")
    print(f"Salario básico: C$ {grossSalary:.2f}")
    print("Deducciones:")
    print(f"  - Deducción básica: {basicPercentage:.2f}% (-C$ {basicDeduction:.2f})")
    print(f"  - INSS: {inssPercentage:.2f}% (-C$ {inssDeduction:.2f})")
    print(f"  - IR: {irPercentage:.2f}% (-C$ {irDeduction:.2f})")
    print(f"Total deducciones: {totalDeductionPercentage:.2f}% (-C$ {totalDeductions:.2f})")
    print(f"Salario neto (C$): C$ {netSalaryNIO:.2f}")
    print(f"Salario neto (USD): ${netSalaryUSD:.2f}")
    print("----------------------------------------\n")


def main():
    clearConsole()
    printSucess("CALCULADORA DE SALARIOS DE COLABORADORES")

    InssDeductionPercentage = 0.07
    baseDeductionPercentage = 0.10

    employeeName, grossSalary = readEmployeeData()

    basicDeduction = calculateBasicDeduction(grossSalary, baseDeductionPercentage)
    inssDeduction = calculateInssDeduction(grossSalary, InssDeductionPercentage)
    irDeduction = calculateEmploymentIncomeTax(grossSalary, InssDeductionPercentage)

    totalDeductions = basicDeduction + inssDeduction + irDeduction
    netSalary = calculateNetSalary(grossSalary, totalDeductions)
    salaryUSD = calculateNIO_USD(netSalary)

    showEmployeeNetSalary(employeeName, grossSalary, basicDeduction, inssDeduction, irDeduction, totalDeductions, netSalary, salaryUSD)


if __name__ == "__main__":
    main()
