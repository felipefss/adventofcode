fun meetReqs(num: String): Boolean {
    if (num.length > 6) return false
    
    var adjMap = mutableMapOf<Char, Int>()
    var increase = true
    for (i in 1 until num.length) {
        if (num[i] == num[i - 1]) {
            val adjs = adjMap.getOrDefault(num[i], 1)
            adjMap[num[i]] = adjs + 1
        }
        if (num[i].toInt() < num[i - 1].toInt()) {
            increase = false
            break
        }
    }

    val adjacent = adjMap.containsValue(2)
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
