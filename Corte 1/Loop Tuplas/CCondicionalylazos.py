{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"1JkGRGqmiKvGw5XCOvdbpf77V5D4S2F1X","timestamp":1725278174876}],"authorship_tag":"ABX9TyOEyqKYltU/c0457yCjKHyu"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"EIkIazctiJVq"},"outputs":[],"source":["for i in range(100, 300):\n","  if (i%12) !=0:\n","    continue\n","    print(i)"]},{"cell_type":"code","source":["while True:\n","\n","    value = int(input(\"Enter a positive integer value: \"))\n","    print(\"Value: \", value)\n","    a = isinstance(value, int)\n","    if a == True and value > 0:\n","        fact = 1\n","        for i in range (1, value + 1):\n","            fact = fact*i\n","        print(f'The factorial of {value} is: ', fact)\n","    else:\n","        print(\"Please, enter a positive integer number\")"],"metadata":{"id":"_v5ZAAmGo9Vf"},"execution_count":null,"outputs":[]}]}