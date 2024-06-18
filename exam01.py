import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import sqlite3

# 初始化資料庫
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        payment INTEGER DEFAULT 0
    )
''')
conn.commit()

# 資料視覺化函數定義

# GDP Data
def plot_gdp_data():
    df = pd.read_csv('D:\\Cloud_Service\\Finalexam\\countrygdpmyself.csv', header=0, encoding='latin1')
    df.columns = ['Year', 'Amount', 'Growth rate']
    df['Amount'] = df['Amount'].str.replace(',', '').astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    amounts = df['Amount']
    growth_rates = df['Growth rate']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    bars = ax1.bar(years, amounts, color='blue', label='Amount (Million)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Amount (Million)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax2 = ax1.twinx()
    line, = ax2.plot(years, growth_rates, color='red', marker='o', label='Growth rate')
    ax2.set_ylabel('Growth rate (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.15))
    plt.title('GDP')
    st.pyplot(fig)

# Earnings Data
def plot_earning_data():
    df = pd.read_csv('D:\\Cloud_Service\\Finalexam\\everyone_GDP_Earning_income_v2.csv', header=0, encoding='latin1')
    df.columns = ['Year', 'PersonalGDP', 'Growth rate', 'PersonalExpenses']
    df['PersonalGDP'] = df['PersonalGDP'].str.replace(',', '').astype(float) / 1e6
    df['PersonalExpenses'] = df['PersonalExpenses'].str.replace(',', '').astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    personal_gdp = df['PersonalGDP']
    growth_rates = df['Growth rate']
    personal_expenses = df['PersonalExpenses']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    bar_width = 0.35
    index = range(len(years))
    bars1 = ax1.bar([i - bar_width/2 for i in index], personal_gdp, bar_width, color='blue', label='PersonalGDP (Million)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('PersonalGDP (Million)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    bars2 = ax1.bar([i + bar_width/2 for i in index], personal_expenses, bar_width, color='orange', alpha=0.5, label='PersonalExpenses (Million)')
    ax1.set_ylabel('Amount(Million)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')
    ax2 = ax1.twinx()
    line, = ax2.plot(years, growth_rates, color='red', marker='o', label='PersonalGDP Growth')
    ax2.set_ylabel('PersonalGDP Growth(%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.15))
    plt.title('Earnings and Related Metrics')
    st.pyplot(fig)

# Overview Industry Data
def plot_overview_industry_data():
    df = pd.read_csv('D:\\Cloud_Service\\Finalexam\\overview_industryGDP.csv', header=0, encoding='latin1')
    df.columns = ['Year', 'geoponics', 'industry', 'Service industry']
    df['geoponics'] = df['geoponics'].str.replace(',', '').astype(float) / 1e6
    df['industry'] = df['industry'].str.replace(',', '').astype(float) / 1e6
    df['Service industry'] = df['Service industry'].str.replace(',', '').astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    geoponics = df['geoponics']
    industry = df['industry']
    service_industry = df['Service industry']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    line1, = ax1.plot(years, geoponics, color='blue', marker='o', label='geoponics (Million)')
    line2, = ax1.plot(years, service_industry, color='orange', marker='o', label='Service industry (Million)')
    ax1.set_ylabel('Amount (Million)')
    ax1.set_xlabel('Year')
    line3, = ax1.plot(years, industry, color='red', marker='o', label='industry (Million)')
    lines = [line1, line2, line3]
    ax1.legend(lines, [line.get_label() for line in lines], loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.title('Overview of Industry Data')
    st.pyplot(fig)

# Detailed Industry GDP Data
def plot_detailed_industry_gdp():
    df = pd.read_csv('D:\\Cloud_Service\\Finalexam\\Detailed_industry_GDP.csv', header=0, encoding='latin1')
    df.columns = df.columns.str.strip()
    expected_columns = ['Year', 'geoponics', 'manufacturing', 'Electricity and gas', 'Construction',
                        'Wholesale and Retail', 'Transport and Warehouse', 'Finance and Insurance', 'Public and social security']
    for column in expected_columns[1:]:
        df[column] = df[column].str.replace(',', '', regex=False).str.replace('(', '-', regex=False).str.replace(')', '', regex=False).astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    industry_data = {col: df[col] for col in expected_columns[1:]}
    fig, ax1 = plt.subplots(figsize=(12, 6))
    lines = []
    for industry, data in industry_data.items():
        line, = ax1.plot(years, data, marker='o', label=f'{industry} (Million)')
        lines.append(line)
    ax1.set_ylabel('Amount (Million)')
    ax1.set_xlabel('Year')
    ax1.legend(lines, [line.get_label() for line in lines], loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.title('Detailed Industry GDP')
    st.pyplot(fig)

# GDP Expenditure Data
def plot_gdp_expenditure_data():
    df = pd.read_csv('D:\\Cloud_Service\\Finalexam\\GDPExpenditure.csv', header=0, encoding='latin1')
    df.columns = ['Year', 'Private consumption', 'Government consumption', 'Fixed capital', 'Inventory changes', 'Export', 'Import']
    for column in df.columns[1:]:
        df[column] = df[column].str.replace(',', '').astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    expenditure_data = {col: df[col] for col in df.columns[1:]}
    fig, ax1 = plt.subplots(figsize=(12, 6))
    lines = []
    for expenditure, data in expenditure_data.items():
        line, = ax1.plot(years, data, marker='o', label=f'{expenditure} (Million)')
        lines.append(line)
    ax1.set_ylabel('Amount (Million)')
    ax1.set_xlabel('Year')
    ax1.legend(lines, [line.get_label() for line in lines], loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.title('GDP Expenditure Data')
    st.pyplot(fig)

# Population Employment Data
def plot_population_employment_data():
    df = pd.read_csv('D:\\Cloud_Service\\Finalexam\\employment_rate.csv', header=0, encoding='latin1')
    df.columns = ['Year', 'Population_15_plus', 'Employment_rate_15_plus', 'Employment_rate_labor_force', 'Unemployment_rate']
    df['Population_15_plus'] = df['Population_15_plus'].str.replace(',', '').astype(float) / 1e3
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    population = df['Population_15_plus']
    employment_rate_15_plus = df['Employment_rate_15_plus']
    employment_rate_labor_force = df['Employment_rate_labor_force']
    unemployment_rate = df['Unemployment_rate']
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    bars = ax1.bar(years, population, color='blue', label='Population (Thousand)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Population (Thousand)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    
    ax2 = ax1.twinx()
    line1, = ax2.plot(years, employment_rate_15_plus, color='red', marker='o', label='Employment rate (15+ years)')
    line2, = ax2.plot(years, employment_rate_labor_force, color='orange', marker='o', label='Employment rate (Labor force)')
    line3, = ax2.plot(years, unemployment_rate, color='green', marker='o', label='Unemployment rate')
    
    ax2.set_ylabel('Rate (%)')
    ax2.tick_params(axis='y', labelcolor='black')
    
    lines = [line1, line2, line3]
    ax2.legend(lines, [line.get_label() for line in lines], loc='upper left', bbox_to_anchor=(0.1, 0.85))
    
    plt.title('Population and Employment Data')
    st.pyplot(fig)

def update_payment_status(username):
    c.execute("UPDATE users SET payment = 1 WHERE username = ?", (username,))
    conn.commit()
    st.session_state['payment'] = True  # 更新 session 狀態中的付費狀態

# 主程式
def main():
    st.title("JimeeFirstWebApp")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['guest_chart_views'] = 0
        st.session_state['payment'] = False

    if st.session_state['logged_in']:
        st.write(f"歡迎，{st.session_state['username']}！")
        st.subheader("選擇要顯示的圖表")

        # 匯入自訂 CSV 檔案功能
        if st.button("匯入自訂 CSV 檔案"):
            uploaded_file = st.file_uploader("選擇要匯入的 CSV 檔案", type=["csv"])
            if uploaded_file is not None:
                try:
                    df_custom = pd.read_csv(uploaded_file, header=0, encoding='latin1')
                    # 在此處理自訂 CSV 檔案的資料視覺化或其他操作
                    # 例如，這裡可以直接顯示匯入的資料框架
                    st.write("以下是匯入的自訂 CSV 檔案資料：")
                    st.write(df_custom.head())

                except Exception as e:
                    st.error(f"匯入檔案時發生錯誤：{e}")

        # 現有的圖表選項
        chart_options = {
            "GDP Data": plot_gdp_data,
            "Earning Data": plot_earning_data,
            "Overview Industry Data": plot_overview_industry_data,
            "Detailed Industry GDP Data": plot_detailed_industry_gdp,
            "GDP Expenditure Data": plot_gdp_expenditure_data,
            "Population Employment Data": plot_population_employment_data
        }

        if 'chart_views' not in st.session_state:
            st.session_state['chart_views'] = 0

        # 顯示圖表選項，限制顯示次數或付費條件
        if st.session_state['payment'] or st.session_state['chart_views'] < 3:
            chart_type = st.selectbox("選擇要顯示的圖表", list(chart_options.keys()))
            if chart_type:
                plot_function = chart_options[chart_type]
                plot_function()
                st.session_state['chart_views'] += 1
        else:
            st.write("您已達到查看圖表的次數上限。請付費以繼續使用更多功能。")
            if st.button("付費繼續使用"):
                st.session_state['show_payment_page'] = True
                st.experimental_rerun()

        if st.button("登出"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.session_state['chart_views'] = 0
            st.session_state['payment'] = False
            st.experimental_rerun()

    else:
        menu = ["登入", "註冊"]
        choice = st.sidebar.selectbox("選擇操作", menu)

        if choice == "登入":
            login()
        elif choice == "註冊":
            signup()

        st.write("您目前以訪客身分查看此應用。請登入以查看圖表。")


def login():
    st.subheader("請登入")
    
    username = st.text_input("用戶名")
    password = st.text_input("密碼", type="password")

    if st.button("登入"):
        user = validate_login(username, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['payment'] = False
            st.success("登入成功！")
            st.experimental_rerun()
        else:
            st.error("用戶名或密碼錯誤。")

def signup():
    st.subheader("註冊新帳戶")
    
    new_username = st.text_input("新用戶名")
    new_password = st.text_input("新密碼", type="password")

    if st.button("註冊"):
        if not validate_signup(new_username):
            create_user(new_username, new_password)
            st.success("註冊成功，請登入！")
        else:
            st.error("用戶名已存在，請選擇其他用戶名。")

def validate_login(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return c.fetchone()

def validate_signup(username):
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    return c.fetchone()

def create_user(username, password):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()


def show_payment_page():
    st.subheader("付費繼續使用")
    st.write("請選擇您的付費方案：")
    plans = ["1個月 - NT$100", "3個月 - NT$250", "1年 - NT$900"]
    plan = st.selectbox("選擇方案", plans)
    if st.button("付款"):
        st.success(f"已成功購買 {plan} 方案！")
        st.session_state['chart_views'] = 0  # 重置查看次數
        st.session_state['payment'] = True
        st.session_state['show_payment_page'] = False
        st.experimental_rerun()

if __name__ == "__main__":
    if 'show_payment_page' in st.session_state and st.session_state['show_payment_page']:
        show_payment_page()
    else:
        main()
