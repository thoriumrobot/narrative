import random
from langchain_ollama import OllamaLLM

# 1. Placeholder lists for Alice (Wound) and Botanical (Medicine) readings
# Fill these with your actual 90 Wound readings and 66 Medicine readings.
alice_readings = [
    "All in the Golden Afternoon. Time to create. An imaginative idea. Inspiration takes hold. Talent and ability. The muse touches down in your life - get ready!",
    "All in the Golden Afternoon Reversed. Feeling Dull, uninspired, mundane. Believing you lack creativity. Dissatisfaction with your work. Negative self-talk.",
    "I Wonder What Will Happen Next? A longing for excitement. Wonder at what is meant to take place next. Someone who is comfortable but vaguely dissatisfied. Be ready for a challenge and new experiences.",
    "I Wonder What Will Happen Next? Reversed. Attachment to habit. Locked into stultifying sameness. Comfort over adventure. A lack of curiosity. Satisfaction remaining within the same world, in a repetitive cycle.",
    "Follow the White Rabbit. A wondrous opportunity is going to break through your ordinary reality and give you the chance to change your world and your perception, forever.",
    "Follow the White Rabbit Reversed. Opportunity after opportunity, chance after chance to have adventures, but not feeling ready. Thinking you must think on it, take more timeor even that the opportunity will come by again. Hesitation is costing you a omre exciting, dynamic and enchanted life.",
    "Alice Wound Reading 1: ...",
    "Alice Wound Reading 2: ...",
    "Alice Wound Reading 3: ...",
    "Alice Wound Reading 1: ...",
    "Alice Wound Reading 2: ...",
    "Alice Wound Reading 3: ...",
    "Alice Wound Reading 1: ...",
    "Alice Wound Reading 2: ...",
    "Alice Wound Reading 3: ...",
    "Alice Wound Reading 90: ..."
]

botanical_readings = [
    "Botanical Medicine Reading 1: ...",
    "Botanical Medicine Reading 2: ...",
    "Botanical Medicine Reading 3: ...",
    # ...
    "Botanical Medicine Reading 66: ..."
]

# 2. The 8 effects of trauma
effects = [
    "1. Sensitivity",
    "2. Inattention",
    "3. Obsession",
    "4. Depression",
    "5. Anger",
    "6. Panic",
    "7. Guilt",
    "8. Dissociation"
]

def generate_divination():
    """
    Returns a dictionary of 8 trauma effects, each with a randomly
    drawn Wound (from Alice readings) and Medicine (from Botanical readings),
    ensuring no index is repeated in the same reading.
    """
    # Select 8 unique indices from the Alice readings
    wound_indices = random.sample(range(len(alice_readings)), len(effects))
    # Select 8 unique indices from the Botanical readings
    medicine_indices = random.sample(range(len(botanical_readings)), len(effects))

    readings = {}
    for i, effect in enumerate(effects):
        wound = alice_readings[wound_indices[i]]
        medicine = botanical_readings[medicine_indices[i]]
        readings[effect] = {
            "Wound": wound,
            "Medicine": medicine
        }
    return readings

def reading_to_string(reading):
    """
    Helper function to create a friendly string representation
    of the reading dictionary.
    """
    lines = []
    for effect, cards in reading.items():
        lines.append(f"{effect}\n  Wound: {cards['Wound']}\n  Medicine: {cards['Medicine']}\n")
    return "\n".join(lines)

# 3. The function to generate interpersonal events from an offline LLM
def generate_interpersonal_events(character1, character2):
    # Initialize the LLaMA 3.1 8B model (make sure you have this model available offline)
    llm = OllamaLLM(model="llama3.1:8b")

    # Convert dict-based readings into strings
    char1_str = reading_to_string(character1)
    char2_str = reading_to_string(character2)

    # Construct the prompt
    prompt = f"""
Objective: Generate three interpersonal events that advance the narrative.

Character traits format: For each of the 8 effects of trauma, the nature of the wound and the "medicine", i.e. the character arc that would serve as treatment, are indicated.

Character 1:
{char1_str}

Character 2:
{char2_str}

Please provide three possible interpersonal events that could occur between these characters, each propelling the story forward.
    """

    # Generate and return the response
    response = llm.invoke(prompt)
    return response

# 4. Generate two separate readings, then generate events
if __name__ == "__main__":
    # First character’s reading
    character1 = generate_divination()
    # Second character’s reading
    character2 = generate_divination()

    # Generate the interpersonal events
    events = generate_interpersonal_events(character1, character2)
    print(events)
