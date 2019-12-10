fun meetReqs(num: String): Boolean {
    if (num.length > 6) return false

    var adjacent = false
    var increase = true
    for (i in 1 until num.length) {
        if (num[i] == num[i - 1]) {
            adjacent = true
        }
        if (num[i].toInt() < num[i - 1].toInt()) {
            increase = false
            break
        }
    }

    return adjacent && increase
}

fun main() {
    val input = "156218-652527".split('-')
    val range = listOf(input[0].toInt(), input[1].toInt())

    var totalPasswords = 0
    for (i in range[0]..range[1]) {
        if (meetReqs(i.toString())) totalPasswords++
    }
    println(totalPasswords)
}
