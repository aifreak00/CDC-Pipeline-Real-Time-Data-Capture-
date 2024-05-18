import faker  # Importing faker library for generating fake data
import psycopg2  # Importing psycopg2 library for PostgreSQL database operations
from datetime import datetime  # Importing datetime module for timestamp
import random  # Importing random module for generating random data

fake = faker.Faker()  # Creating an instance of the Faker class

def generate_transaction():
    # Generating a fake user profile
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),  # Generating a fake UUID for transaction ID
        "userId": user['username'],  # Extracting username from the fake user profile
        "timestamp": datetime.utcnow().timestamp(),  # Getting current UTC timestamp
        "amount": round(random.uniform(10, 1000), 2),  # Generating a random amount
        "currency": random.choice(['USD', 'GBP']),  # Choosing a random currency
        'city': fake.city(),  # Generating a fake city name
        "country": fake.country(),  # Generating a fake country name
        "merchantName": fake.company(),  # Generating a fake company name
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),  # Choosing a random payment method
        "ipAddress": fake.ipv4(),  # Generating a fake IPv4 address
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),  # Choosing a random voucher code
        'affiliateId': fake.uuid4()  # Generating a fake UUID for affiliate ID
    }

def create_table(conn):
    cursor = conn.cursor()

    # Creating a table named 'transactions' if it doesn't already exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255),
            timestamp TIMESTAMP,
            amount DECIMAL,
            currency VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            merchant_name VARCHAR(255),
            payment_method VARCHAR(255),
            ip_address VARCHAR(255),
            voucher_code VARCHAR(255),
            affiliateId VARCHAR(255)
        )
        """)

    cursor.close()
    conn.commit()

if __name__ == "__main__":
    # Connecting to the PostgreSQL database
    conn = psycopg2.connect(
        host='localhost',
        database='financial_db',
        user='postgres',
        password='postgres',
        port=5432
    )

    create_table(conn)  # Creating the 'transactions' table if it doesn't exist

    transaction = generate_transaction()  # Generating a fake transaction
    cur = conn.cursor()
    print(transaction)  # Printing the generated transaction for verification

    # Inserting the generated transaction data into the 'transactions' table
    cur.execute(
        """
        INSERT INTO transactions(transaction_id, user_id, timestamp, amount, currency, city, country, merchant_name, payment_method, 
        ip_address, affiliateId, voucher_code)
        VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (transaction["transactionId"], transaction["userId"], datetime.fromtimestamp(transaction["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
              transaction["amount"], transaction["currency"], transaction["city"], transaction["country"],
              transaction["merchantName"], transaction["paymentMethod"], transaction["ipAddress"],
              transaction["affiliateId"], transaction["voucherCode"])
    )

    cur.close()
    conn.commit()
