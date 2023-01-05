func twoSum(numbers []int, target int) []int {
    l_idx, r_idx := 0, len(numbers) - 1
    for l_idx < r_idx {
        total := numbers[l_idx] + numbers[r_idx]

        if total == target {
            return []int{l_idx+1, r_idx+1}
        } else if total > target {
            r_idx -= 1
        } else {
            l_idx += 1
        }
    }
    return nil
}