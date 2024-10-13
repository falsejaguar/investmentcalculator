import sys
from PySide6 import QtWidgets as qtw
from myUi import Ui_MainWindow

class mWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeUIState()
        self.goButton.clicked.connect(self.calculateInvestment)
        self.checkBox.stateChanged.connect(self.initializeUIState)
        self.show()

    def initializeUIState(self):
        # Toggle visibility of advanced widgets
        if self.checkBox.isChecked():
           # self.advancedLabel.setVisible(True)
            self.dailyRadioButton.setVisible(True)
            self.monthlyRadioButton.setVisible(True)
            self.quarterlyRadioButton.setVisible(True)
            self.adAmount.setVisible(True)
            self.divCagr.setVisible(True)
            self.estAp.setVisible(True)
            self.l_additionLabel.setVisible(True)
            self.l_apLabel.setVisible(True)
            self.l_cagrLabel.setVisible(True)
            
            #self.advancedLayout.setVisible(True)
        else:
           # self.advancedLabel.setVisible(False)
            self.dailyRadioButton.setVisible(False)
            self.monthlyRadioButton.setVisible(False)
            self.quarterlyRadioButton.setVisible(False)
            self.adAmount.setVisible(False)
            self.divCagr.setVisible(False)
            self.estAp.setVisible(False)
            self.l_additionLabel.setVisible(False)
            self.l_apLabel.setVisible(False)
            self.l_cagrLabel.setVisible(False)
            #self.advancedLayout.setVisible(False)

    def calculateInvestment(self):
        try:
            initialInvestment = float(self.inAmount.text())
            interestRate = float(self.intRate.text()) / 100
            
            # Check if simple mode (checkbox unchecked) or compound mode (checkbox checked)
            if not self.checkBox.isChecked():
                # Simple Interest Mode
                final_investment = initialInvestment * (1 + interestRate)
                
                for year in range(1, 12):
                    getattr(self, f"yr{year}").display(f"{final_investment:.2f}")
                    
                    # Calculate next year's investment
                    final_investment *= (1 + interestRate)
            
            else:
                # Compound Interest Mode
                additionalInvestment = float(self.adAmount.text())
                dividendCagr = float(self.divCagr.text()) / 100
                appreciationRate = float(self.estAp.text()) / 100
                dailyRate = interestRate / 365
                monthlyRate = interestRate / 12
                quarterlyRate = interestRate / 4

                investment = initialInvestment
                for year in range(1, 12):
                    if self.dailyRadioButton.isChecked():
                        for day in range(365):
                            investment += additionalInvestment / 30  # Spread additional investment over the month
                            investment *= (1 + dailyRate)
                    elif self.monthlyRadioButton.isChecked():
                        for month in range(12):
                            investment += additionalInvestment
                            investment *= (1 + monthlyRate)
                    else:
                        for quarter in range(4):
                            investment *= (1 + quarterlyRate)
                            investment += additionalInvestment * 3  # Add 3 months' worth of additional investment
                    
                    investment *= (1 + dividendCagr)
                    investment *= (1 + appreciationRate)
                    formatted_investment = f"{investment:.2f}"
                    getattr(self, f"yr{year}").display(formatted_investment)
                    
                    # Save the current investment amount for the next year
                    if year < 11:
                        next_year_investment = investment
                        investment = next_year_investment
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = mWindow()
    window.show()
    sys.exit(app.exec())