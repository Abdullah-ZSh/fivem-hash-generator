# MIT License - (c) 2025 Abdulah-ZSh

def get_hash_key(text: str) -> int:
    """
    Calculate the GTA V / FiveM hash key (Jenkins One-at-a-Time).
    Automatically lowercases the input.
    """
    key = 0
    text = text.lower()
    for c in text:
        key += ord(c)
        key &= 0xFFFFFFFF
        key += (key << 10)
        key &= 0xFFFFFFFF
        key ^= (key >> 6)
    key += (key << 3)
    key &= 0xFFFFFFFF
    key ^= (key >> 11)
    key += (key << 15)
    key &= 0xFFFFFFFF
    return key


def main():
    print("🔧 GTA V / FiveM Hash Generator By Abdulah-ZSh")
    print("Type a model name (e.g., sultan, futo, police):")
    
    try:
        while True:
            vehicle_name = input("\n🔤 Enter Vehicle Code (or 'exit' to quit): ").strip()
            if vehicle_name.lower() in ['exit', 'quit']:
                print("👋 Exiting. Good luck!")
                break
            hash_key = get_hash_key(vehicle_name)
            print(f"🔑 Vehicle Hash for '{vehicle_name}': {hash_key}")
    except KeyboardInterrupt:
        print("\n👋 Exiting. Goodbye!")


if __name__ == "__main__":
    main()
