import hashlib

def hash_string(input_string):
    # 创建 SHA-256 哈希对象
    sha256_hash = hashlib.sha256()
    
    # 将字符串编码为字节并更新哈希对象
    sha256_hash.update(input_string.encode())
    
    # 获取最终的哈希值（十六进制格式）
    hashed_string = sha256_hash.hexdigest()
    
    return hashed_string

# 示例字符串
input_string = "Hello"

# 计算哈希值
hashed_value = hash_string(input_string)

print(f"Original string: {input_string}")
print(f"SHA-256 Hash: {hashed_value}")
