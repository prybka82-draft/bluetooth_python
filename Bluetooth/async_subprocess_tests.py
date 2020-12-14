import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    #out, err = await proc.communicate()

    t = bytearray("", encoding='ascii')

    line = await proc.stdout.readline()
    print(line.decode('ascii').rstrip())

    line = await proc.stdout.readline()
    print(line.decode('ascii').rstrip())

    line = await proc.stdout.readline()
    print(line.decode('ascii').rstrip())

    proc.w

    proc.terminate()




