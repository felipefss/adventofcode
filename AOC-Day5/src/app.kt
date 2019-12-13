import java.io.File

fun doOperation(op: Int, list: Collection<Int>, index: Int, params: List<Int>): MutableList<Int> {
    val newCode = list.toMutableList()

    val inputIndex1: Int = if (params[0] == 0) newCode[index+1] else (index + 1)
    val inputIndex2: Int = if (params[1] == 0) newCode[index+2] else (index + 2)
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

fun doIO(op: Int, list: Collection<Int>, index: Int, paramC: Int): MutableList<Int> {
    val newCode = list.toMutableList()

    val outputIndex: Int = if (paramC == 1 && op == 4) (index + 1) else newCode[index+1]

    when (op) {
        3 -> {
            print("Input (Int): ")
            val input = Integer.valueOf(readLine())
            newCode[outputIndex] = input
            println("")
        }
        4 -> {
            println("Output at index ${index}: ${newCode[outputIndex]}")
        }
    }
    return newCode
}

fun readParams(code: String): Pair<List<Int>, Int> {
    val opcode: Int = code.takeLast(2).toString().toInt()
    val params = code.dropLast(2).reversed().map { it.toString().toInt() }.toList()
    val finalParams = mutableListOf<Int>()

    for (i in 0..2) {
        finalParams.add(params.getOrElse(i) { 0 })
    }

    return Pair(finalParams, opcode)
}

fun readOpCode(intCode: Collection<Int>) {
    var newCode = intCode.toMutableList()
    var i = 0

    while(i < newCode.size) {
        val (params, opcode) = readParams(newCode[i].toString())
        when (opcode) {
            1, 2 -> {
                newCode = doOperation(opcode, newCode, i, params)
                i += 4
            }
            3, 4 -> {
                newCode = doIO(opcode, newCode, i, params[0])
                i += 2
            }
            99 -> {
                return
            }
            else -> throw Exception("Error found on input")
        }
    }
}

fun main() {
    val intCode = mutableListOf<Int>()
        File("input.txt").forEachLine { str ->
            val strList = str.split(',')
            strList.map { intCode.add(it.toInt()) }
        }

    readOpCode(intCode)
//    println("\nDiagnostic code: $diagCode")
//    val code = "143"
//    val opcode: Int = code.takeLast(2).toString().toInt()
//    val params = code.dropLast(2).reversed().map { it.toString().toInt() }.toMutableList()
//    val finalParams = mutableListOf<Int>()
//
//    for (i in 0..2) {
//        finalParams.add(params.getOrElse(i) { 0 })
//    }
//    println(finalParams)
//    println(opcode)
}