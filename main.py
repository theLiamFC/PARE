from openAIAlchemy import openAIAlchemy
import serial_interface
import asyncio
import sys

### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"
### Arduino Alvik ID
aa_id = "asst_NiIdeWySoj4RYIRU7t6r2mpG"
### Ai Alchemist ID
aa_id = "asst_8WN5ksXpnNaBeAr1IKrLq4yd"

### General test thread
# thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


async def main():
    # Assuming `instance` is an instance of the class containing your run method
    AI_interface = openAIAlchemy(aa_id, debug=True)

    result = await AI_interface.run(
        "write code to move the bot forward. There are motors in ports A and B."
    )
    print(result)

    # code, response = AI_interface.extract_code(result)
    # print(response)
    # serial_response = serial_interface.serial_write(bytes(code, 'utf-8'))
    # print(serial_response)


# async def interfaceLoop(AI_interface):
#     userPrompt = input("What would you like your spike prime to do today?")
#         while userPrompt != "E":
#         result = await AI_interface.run(userPrompt)
#         code, response = AI_interface.extract_code(result)
#         replReply = serial_interface.serial_write(bytes(code, 'utf-8'))

# Run the main function in the event loop
if __name__ == "__main__":
    # serial_interface.test_serial()
    asyncio.run(main())
