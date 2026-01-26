package com.example.calculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import java.text.DecimalFormat

class MainActivity : AppCompatActivity() {

    private lateinit var tvDisplay: TextView
    private var currentNumber = ""
    private var previousNumber = ""
    private var operator = ""
    private var isNewOperation = true

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        tvDisplay = findViewById(R.id.tvDisplay)

        // Number buttons
        val btn0 = findViewById<Button>(R.id.btn0)
        val btn1 = findViewById<Button>(R.id.btn1)
        val btn2 = findViewById<Button>(R.id.btn2)
        val btn3 = findViewById<Button>(R.id.btn3)
        val btn4 = findViewById<Button>(R.id.btn4)
        val btn5 = findViewById<Button>(R.id.btn5)
        val btn6 = findViewById<Button>(R.id.btn6)
        val btn7 = findViewById<Button>(R.id.btn7)
        val btn8 = findViewById<Button>(R.id.btn8)
        val btn9 = findViewById<Button>(R.id.btn9)
        val btnDecimal = findViewById<Button>(R.id.btnDecimal)

        // Operator buttons
        val btnAdd = findViewById<Button>(R.id.btnAdd)
        val btnSubtract = findViewById<Button>(R.id.btnSubtract)
        val btnMultiply = findViewById<Button>(R.id.btnMultiply)
        val btnDivide = findViewById<Button>(R.id.btnDivide)
        val btnEquals = findViewById<Button>(R.id.btnEquals)
        val btnClear = findViewById<Button>(R.id.btnClear)
        val btnBackspace = findViewById<Button>(R.id.btnBackspace)

        // Set click listeners for numbers
        val numberButtons = listOf(btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        for (button in numberButtons) {
            button.setOnClickListener { onNumberClick(button.text.toString()) }
        }

        btnDecimal.setOnClickListener { onDecimalClick() }

        // Set click listeners for operators
        btnAdd.setOnClickListener { onOperatorClick("+") }
        btnSubtract.setOnClickListener { onOperatorClick("-") }
        btnMultiply.setOnClickListener { onOperatorClick("*") }
        btnDivide.setOnClickListener { onOperatorClick("/") }
        btnEquals.setOnClickListener { onEqualsClick() }
        btnClear.setOnClickListener { onClearClick() }
        btnBackspace.setOnClickListener { onBackspaceClick() }
    }

    private fun onNumberClick(number: String) {
        if (isNewOperation) {
            currentNumber = number
            isNewOperation = false
        } else {
            if (currentNumber == "0") {
                currentNumber = number
            } else {
                currentNumber += number
            }
        }
        updateDisplay(currentNumber)
    }

    private fun onDecimalClick() {
        if (isNewOperation) {
            currentNumber = "0."
            isNewOperation = false
        } else if (!currentNumber.contains(".")) {
            currentNumber += "."
        }
        updateDisplay(currentNumber)
    }

    private fun onOperatorClick(op: String) {
        if (!isNewOperation || operator.isNotEmpty()) {
            // Calculate the result if there was a previous operation
            if (previousNumber.isNotEmpty() && currentNumber.isNotEmpty() && operator.isNotEmpty()) {
                calculateResult()
            } else {
                // Store the current number as previous number if this is the first operation
                previousNumber = currentNumber
            }
        }
        
        operator = op
        isNewOperation = true
    }

    private fun onEqualsClick() {
        if (previousNumber.isNotEmpty() && currentNumber.isNotEmpty() && operator.isNotEmpty()) {
            calculateResult()
            operator = ""
        }
    }

    private fun calculateResult() {
        try {
            val result = performCalculation("$previousNumber $operator $currentNumber")
            
            // Format the result to avoid unnecessary decimal places
            val formattedResult = if (result % 1 == 0.0) {
                result.toInt().toString()
            } else {
                // Only keep up to 8 decimal places to avoid overflow
                "%.8f".format(result).trimEnd('0').trimEnd('.')
            }
            
            tvDisplay.text = formattedResult
            previousNumber = formattedResult
            currentNumber = formattedResult
            isNewOperation = true
        } catch (e: Exception) {
            Toast.makeText(this, "Error in calculation", Toast.LENGTH_SHORT).show()
            resetCalculator()
        }
    }

    private fun performCalculation(expression: String): Double {
        // Parse the expression string to extract operands and operator
        val parts = expression.split(" ")
        if (parts.size != 3) throw IllegalArgumentException("Invalid expression")
        
        val left = parts[0].toDouble()
        val op = parts[1]
        val right = parts[2].toDouble()
        
        return when (op) {
            "+" -> left + right
            "-" -> left - right
            "*" -> left * right
            "/" -> {
                if (right == 0.0) {
                    throw ArithmeticException("Division by zero")
                }
                left / right
            }
            else -> throw IllegalArgumentException("Unknown operator: $op")
        }
    }

    private fun onClearClick() {
        resetCalculator()
        updateDisplay("0")
    }

    private fun onBackspaceClick() {
        if (currentNumber.isNotEmpty()) {
            currentNumber = if (currentNumber.length == 1) {
                "0"
            } else {
                currentNumber.substring(0, currentNumber.length - 1)
            }
            updateDisplay(currentNumber)
        }
    }

    private fun updateDisplay(value: String) {
        tvDisplay.text = value
    }

    private fun resetCalculator() {
        currentNumber = ""
        previousNumber = ""
        operator = ""
        isNewOperation = true
    }
}