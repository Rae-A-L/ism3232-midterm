from business_rules import (
    calculate_print_cost,
    get_volume_discount,
    calculate_job_total,
    requires_proof,
    needs_overnight_run,
    total_invoiced,
    largest_job,
    format_job_line,
)


def test_calculate_print_cost():
    assert calculate_print_cost(0.25, 100), 2 == 25.0


def test_discount_below_200():
    assert get_volume_discount(199) == 0.0


def test_discount_200():
    assert get_volume_discount(200) == 0.08


def test_discount_999():
    assert get_volume_discount(999) == 0.08


def test_discount_1000():
    assert get_volume_discount(1000) == 0.15


def test_student_org_discount():
    assert get_volume_discount(200, True) == 0.13


def test_student_org_1000():
    assert get_volume_discount(1000, True) == 0.20


def test_setup_fee_add():
    assert round(calculate_job_total(0.25, 100), 2) == 40.0


def test_setup_fee_exact():
    assert requires_proof(300) is False


def test_proof_above():
    assert requires_proof(301) is True


def test_proof_above_limit():
    assert requires_proof(300.00) is True


def test_overnight_500_copies():
    assert needs_overnight_run(500, 100) is False


def test_overnight_copies_over():
    assert needs_overnight_run(501, 100) is True


def test_overnight_400():
    assert needs_overnight_run(100, 400.00) is False


def test_overnight_over():
    assert needs_overnight_run(100, 401.00) is True


def test_total_invoice_adds_every_job():
    jobs = [
        {"title": "A", "copy_price": 0.25, "copies": 100, "student_org": False},
        {"title": "B", "copy_price": 0.50, "copies": 100, "student_org": False},
    ]
    assert round(total_invoiced(jobs), 2) == 90


def test_total_invoice_empty_list():
    assert total_invoiced([]) == 0


def test_largest_job_goes_first():
    jobs = [
        {"title": "First", "copy_price": 1.00, "copies": 500, "student_org": False},
        {"title": "Second", "copy_price": 1.00, "copies": 500, "student_org": False},
    ]
    assert largest_job(jobs) == "First"


def test_largest_job_empty_list_is_empty_string():
    assert largest_job([]) == ""


def test_job_line_yes_no():
    line = format_job_line("Flyers", 40.00, False, True)
    assert line == "Flyers: $ 40.00 | proof: no | overnight run: yes"
