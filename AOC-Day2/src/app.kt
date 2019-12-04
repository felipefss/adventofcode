import java.io.File
import java.lang.Integer.parseInt

fun readOpCode(intCode: Collection<Int>): Collection<Int> {
    val newCode = intCode.toList()

    for (i in newCode.indices) {
        val input1: Int = newCode[i+1]
        val input2: Int = newCode[i+2]
        val output: Int = newCode[i+3]

        when (i) {
            1 -> {
                
            }
            2 -> {

            }
            99 -> {

            }
            else -> throw Exception("Error found on input")
        }
    }
}

fun main() {
    val intCode = mutableListOf<Int>()
    File("input.txt").forEachLine { intCode.add(parseInt(it)) }
}