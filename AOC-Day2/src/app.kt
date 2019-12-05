import java.io.File

fun calculate(op: Int, list: Collection<Int>, index: Int): MutableList<Int> {
    val newCode = list.toMutableList()

    val inputIndex1: Int = newCode[index+1]
    val inputIndex2: Int = newCode[index+2]
    val outputIndex: Int = newCode[index+3]
    val a = newCode[inputIndex1]
    val b = newCode[inputIndex2]

    when (op) {
        1 -> {
            newCode[outputIndex] = a + b
        }
        2 -> {
            newCode[outputIndex] = a * b
        }
    }

    return newCode
}

fun readOpCode(intCode: Collection<Int>): Collection<Int> {
    var newCode = intCode.toMutableList()

    for (i in newCode.indices step 4) {
        when (newCode[i]) {
            1 -> {
                newCode = calculate(1, newCode, i)
            }
            2 -> {
                newCode = calculate(2, newCode, i)
            }
            99 -> {
                return newCode
            }
            else -> throw Exception("Error found on input")
        }
    }

    return newCode
}

fun main() {
    val intCode = File("input.txt").readLines()
    val intCodeList = intCode.toList()
    println(readOpCode(mutableListOf(1,9,10,3,2,3,11,0,99,30,40,50)))
}