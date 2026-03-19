# PostgreSQL Installation & Setup Guide

## Step 1: Install PostgreSQL on Windows

### Option A: Download Official Installer (Recommended)
1. Go to: https://www.postgresql.org/download/windows/
2. Click "Download the installer" (EnterpriseDB)
3. Download the latest version (16.x or newer)
4. Run the installer

### Installation Steps:
1. **Installation Directory**: Keep default (`C:\Program Files\PostgreSQL\16`)
2. **Components**: Select all (PostgreSQL Server, pgAdmin 4, Stack Builder, Command Line Tools)
3. **Data Directory**: Keep default
4. **Password**: Enter `MentalHealthApp2026!` (or your preferred password)
   - ⚠️ IMPORTANT: Remember this password! It's for the 'postgres' superuser
5. **Port**: Keep default (5432)
6. **Locale**: Keep default
7. Click "Next" and then "Finish"

### Option B: Using Winget (if available)
```powershell
winget install PostgreSQL.PostgreSQL
```

### Option C: Using Chocolatey (if available)
```powershell
choco install postgresql
```

## Step 2: Verify Installation

Open a new Command Prompt or PowerShell and run:
```bash
psql --version
```

You should see something like: `psql (PostgreSQL) 16.x`

## Step 3: Set Environment Variables (if needed)

If `psql` command is not found, add PostgreSQL to your PATH:
1. Search for "Environment Variables" in Windows
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "System variables", find "Path" and click "Edit"
5. Click "New" and add: `C:\Program Files\PostgreSQL\16\bin`
6. Click "OK" on all dialogs
7. **Restart your terminal**

## Step 4: Test Connection

Open Command Prompt and run:
```bash
psql -U postgres
```

When prompted, enter your password: `MentalHealthApp2026!`

You should see the PostgreSQL prompt: `postgres=#`

Type `\q` to exit.

## Step 5: Install Python Dependencies

In your project directory, run:
```bash
pip install -r requirements_postgres.txt
```

Or install directly:
```bash
pip install psycopg2-binary
```

## Step 6: Run the Demo Program

```bash
python postgres_demo.py
```

## Default Password Information

**Default Credentials:**
- Username: `postgres`
- Password: `MentalHealthApp2026!` (as set during installation)

**To change the password later:**
1. Connect to PostgreSQL: `psql -U postgres`
2. Run: `ALTER USER postgres WITH PASSWORD 'your_new_password';`
3. Update the password in `postgres_demo.py`

## Common Issues

### Issue: "psql: command not found"
**Solution:** PostgreSQL bin directory is not in PATH. Follow Step 3 above.

### Issue: "connection refused"
**Solution:** PostgreSQL service is not running.
- Open Services (Win+R, type `services.msc`)
- Find "postgresql-x64-16" (or similar)
- Right-click and select "Start"

### Issue: "password authentication failed"
**Solution:** Check your password in `postgres_demo.py` matches the one you set during installation.

## Useful Commands

```bash
# Connect to PostgreSQL
psql -U postgres

# List databases
\l

# Connect to a database
\c database_name

# List tables
\dt

# Describe a table
\d table_name

# Quit
\q
```

## Next Steps

After installation and testing, you can:
1. Create a new database for your mental health app
2. Design your schema
3. Integrate with your Python application
4. Consider using an ORM like SQLAlchemy or Django ORM

Good luck! 🚀
