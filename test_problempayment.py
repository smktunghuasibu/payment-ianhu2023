import os.path
from problempayment import main
from tud_test_base import *

def test_pay():
    try:
        exist = os.path.exist("pay.py")
        assert exist == True
    except:
        SystemExit
    
    set_keyboard_input([5])
    main()
    output = get_display_output()

    assert output == [
        "Simple Pay Program\n",
        "How many hours did you work: ",
        "\nPay Stub",
        "\t\tHours: 5",
        "\t\tRate: $25.00",
        "\t\tPay: $125.00",
        "\t\tTax: $15.62",
        "\t\tNet Pay: $109.38"
    ]
