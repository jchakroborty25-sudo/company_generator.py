from Generators.company_generator import generate_company
from Generators.department_generator import generate_department

def main():

    print("=" * 50)
    print("NovaSphere Finance Analytics Platform")
    print("=" * 50)

    generate_company()
    generate_department()

    print("✅ Sprint 2 Complete")

if __name__ == "__main__":
    main()
