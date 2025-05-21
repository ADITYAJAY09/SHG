from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shg_database'

mysql = MySQL(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.form
        required_fields = ['Name', 'Age', 'Caste', 'Education', 'Marital Status',
                         'Household Size', 'Year Joined SHG', 'Role in SHG',
                         'Frequency of Meetings Attended', 'Monthly Savings Amount']
        
        # Validate required fields
        for field in required_fields:
            if field not in data or not data[field]:
                return f"Missing required field: {field}", 400

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO shg_responses (
                name, age, caste, education, marital_status, household_size,
                year_joined, role_in_shg, meeting_frequency, savings_amount,
                loan_details, financial_training, income_increased, income_source,
                skill_development, household_decision, village_meeting,
                independent_travel, confidence, social_support, leadership,
                group_issues, training_needs, suggestions
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data['Name'], data['Age'], data['Caste'], data['Education'], data['Marital Status'],
            data['Household Size'], data['Year Joined SHG'], data['Role in SHG'], data['Frequency of Meetings Attended'],
            data['Monthly Savings Amount'], data.get('Loan Details (Amount, Purpose, Repayment Status)', ''),
            data.get('Financial Training/Support Received', ''), data.get('Has Your Income Increased After Joining SHG? (Yes/No)', ''),
            data.get('If Yes, How?', ''), data.get('Skill Development or Employment Changes', ''),
            data.get('Involvement in Household Financial Decisions (Yes/No)', ''),
            data.get('Participation in Village Meetings (Yes/No)', ''), data.get('Independent Travel for SHG/Market Work (Yes/No)', ''),
            data.get('Do You Feel More Confident Now? (Yes/No)', ''), data.get('Has Your Social Network/Support Increased? (Yes/No)', ''),
            data.get('Community or Leadership Involvement', ''), data.get('Issues Faced in Group Functioning', ''),
            data.get('Training Needs Identified', ''), data.get('Suggestions to Strengthen SHGs', '')
        ))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
