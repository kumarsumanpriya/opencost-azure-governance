package infracost

# Block pull requests that increase monthly cloud spend by more than $500 without budget authorization
default allow = false

max_monthly_delta = 500.0

allow {
    diff := input.diffTotalMonthlyCost
    to_number(diff) <= max_monthly_delta
}

deny[msg] {
    diff := input.diffTotalMonthlyCost
    to_number(diff) > max_monthly_delta
    msg := sprintf("PR cost delta ($%v) exceeds the maximum authorized monthly increase ($%v). VP Approval required.", [diff, max_monthly_delta])
}
