import java.io.File
import java.lang.Integer.parseInt

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
        newCode = when (newCode[i]) {
            1 -> calculate(1, newCode, i)
            2 -> calculate(2, newCode, i)
            99 -> {
                return newCode
            }
            else -> throw Exception("Error found on input")
        }
    }

    return newCode
}

fun main() {
    val intCode = mutableListOf<Int>()
        File("input.txt").forEachLine { str ->
            val strList = str.split(',')
            strList.map { intCode.add(parseInt(it)) }
        }
    
    for (i in 0..99) {
        for (j in 0..99) {
            val cleanIntCode = intCode.toMutableList()
            cleanIntCode[1] = i
            cleanIntCode[2] = j
            val res: List<Int> = readOpCode(cleanIntCode).toList()
            if (res[0] == 19690720) {
                println("noun: $i")
                println("verb: $j")
                println("Answer is ${100 * i + j}")
                return
            }
        }
    }
}