from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QDoubleValidator, QColor, QPalette
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loan Calculator")
        self.setGeometry(100, 100, 400, 500)
        self.UIComponents()
        self.show()

    def UIComponents(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        head = QLabel("Loan Calculator \n SID Bank", self)
        font = QFont('Quicksand', 15)
        font.setBold(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)

        # Adding peach color background
        peach_color = QColor(240, 128, 128)
        palette = QPalette()
        palette.setColor(QPalette.Window, peach_color)
        head.setAutoFillBackground(True)
        head.setPalette(palette)

        layout.addWidget(head)
        layout.addSpacing(20)

        # Horizontal layout for annual interest
        i_layout = QHBoxLayout()
        i_label = QLabel("Annual Interest", self)
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setFont(QFont('Quicksand', 9))
        i_label.setStyleSheet("QLabel {"
                              "border: 2px solid black;"
                              "background: rgba(240, 128, 128, 150);"
                              "}")
        self.rate = QLineEdit()
        onlyDouble = QDoubleValidator()
        onlyDouble.setDecimals(2)
        self.rate.setValidator(onlyDouble)
        self.rate.setFont(QFont('Quicksand', 9))
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFixedSize(200, 30)
        i_layout.addWidget(i_label)
        i_layout.addWidget(self.rate)
        layout.addLayout(i_layout)

        # Horizontal layout for years
        n_layout = QHBoxLayout()
        n_label = QLabel("Years", self)
        n_label.setAlignment(Qt.AlignCenter)
        n_label.setFont(QFont('Quicksand', 9))
        n_label.setStyleSheet("QLabel {"
                              "border: 2px solid black;"
                              "background: rgba(240, 128, 128, 150);"
                              "}")
        self.years = QLineEdit()
        self.years.setValidator(onlyDouble)
        self.years.setFont(QFont('Quicksand', 9))
        self.years.setAlignment(Qt.AlignCenter)
        self.years.setFixedSize(200, 30)
        n_layout.addWidget(n_label)
        n_layout.addWidget(self.years)
        layout.addLayout(n_layout)

        # Horizontal layout for loan amount
        a_layout = QHBoxLayout()
        a_label = QLabel("Amount", self)
        a_label.setAlignment(Qt.AlignCenter)
        a_label.setFont(QFont('Quicksand', 9))
        a_label.setStyleSheet("QLabel {"
                              "border: 2px solid black;"
                              "background: rgba(240, 128, 128, 150);"
                              "}")
        self.amount = QLineEdit()
        self.amount.setValidator(onlyDouble)
        self.amount.setFont(QFont('Quicksand', 9))
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setFixedSize(200, 30)
        a_layout.addWidget(a_label)
        a_layout.addWidget(self.amount)
        layout.addLayout(a_layout)

        layout.addStretch()

        # Calculate button
        calculate = QPushButton("Compute Payment", self)
        calculate.setGeometry(125, 270, 150, 40)
        calculate.clicked.connect(self.calculate_action)
        layout.addWidget(calculate)

        # Output labels with increased size and centered alignment
        output_layout = QVBoxLayout()
        output_layout.setAlignment(Qt.AlignCenter)

        self.m_payment = QLabel(self)
        self.m_payment.setAlignment(Qt.AlignCenter)
        self.m_payment.setFont(QFont('Quicksand', 11))
        self.m_payment.setStyleSheet("QLabel {"
                                     "border: 3px solid black;"
                                     "background: white;"
                                     "}")
        self.m_payment.setFixedSize(300, 80)
        output_layout.addWidget(self.m_payment)

        self.t_payment = QLabel(self)
        self.t_payment.setAlignment(Qt.AlignCenter)
        self.t_payment.setFont(QFont('Quicksand', 11))
        self.t_payment.setStyleSheet("QLabel {"
                                     "border: 3px solid black;"
                                     "background: white;"
                                     "}")
        self.t_payment.setFixedSize(300, 80)
        output_layout.addWidget(self.t_payment)

        layout.addLayout(output_layout)

    def calculate_action(self):
        # Check if any input field is empty
        if self.rate.text().strip() == '' or self.years.text().strip() == '' or self.amount.text().strip() == '' or self.rate.text().strip() == '0' or self.years.text().strip() == '0' or self.amount.text().strip() == '0':
            QMessageBox.warning(self, "Error", "Please fill in non-zero value for all the fields.")
            return
        
        try:
            rate = float(self.rate.text())
            years = float(self.years.text())
            amount = float(self.amount.text())

            monthly_rate = rate / (12 * 100)
            number_of_payments = years * 12

            if monthly_rate != 0:
                monthly_payment = amount * monthly_rate * ((1 + monthly_rate) ** number_of_payments) / (((1 + monthly_rate) ** number_of_payments) - 1)
            else:
                monthly_payment = amount / number_of_payments

            total_payment = monthly_payment * number_of_payments

            self.m_payment.setText(f"Monthly Payment: ₹{monthly_payment:.2f}")
            self.t_payment.setText(f"Total Payment: ₹{total_payment:.2f}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numeric values.")

# Main application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
