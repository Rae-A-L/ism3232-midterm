def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Returns the print cost before any discount."""
    return copy_price * copies 

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Returns the discount rate as a decimal  """
    if copies < 200:
        discount = 0.00
    elif copies <= 999:
        discount = .08 
    else:
        discount = .15
    if copies >= 200 and student_org:
        discount = discount + .05
    return discount 

    
def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Returns the job total for one job: the discounted cost, plus the setup fee when it applies."""
    cost = calculate_print_cost(copy_price, copies)

    discount = get_volume_discount(copies, student_org)

    discounted_cost = cost * (1 - discount)
    return discounted_cost

def requires_proof(total: float) -> bool:
    """Returns True when the job total requires a printed proof, otherwise False."""
    if  total > 300:
        return True
    else:
        return False 
    
def needs_overnight_run(copies: int, total: float) -> bool:
    """Returns True when the job needs an overnight press run, otherwise False."""
    if copies > 500 or total > 400:
     return True 
    else:
        return False

def total_invoiced(jobs: list) -> float:
    """Returns the sum of the job totals for every job in the list."""
    total = 0.0
    for job in jobs:
        total += calculate_job_total (job["copy_price"],job["copies"],job["student_org"]) 
        return total 
    

def largest_job(jobs: list) -> str:
    """Returns the title of the job with the highest total."""
    largest_job = ""
    largest = 0.0
    for job in jobs:
        total = calculate_job_total( 
            job["copy_price"], job["copies"], job["student_org"]
        )
        if total > largest:
            largest = total 
            largest_job = job["title"] 
    return largest_job


def format_job_line(title:str, total: float, proof: bool, overnight_run: bool) -> str:
    """Returns one line of the report"""
    proof_text = "no"
    if proof:
        proof_text = "yes"
    overnight_text = "no"
    if overnight_run:
        overnight_text = "yes"
    return f"{title}: ${total: .2f} | proof: {proof_text} | overnight run: {overnight_text}"
