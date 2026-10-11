"""
AURA MATRIX: Dialogic Engine Core (v2.1)
Dependencies: google-antigravity, asyncio
"""
import asyncio
from google.antigravity import Agent, GenerationConfig

class SocraticFSM:
    def __init__(self):
        self.socrates = Agent(
            model="claude-3-5-sonnet",
            system_instruction="You are Socrates. Do not answer questions. Ask exactly one question per turn to expose logical flaws in the user's premise.",
            generation_config=GenerationConfig(temperature=0.1)
        )

    async def step(self, user_input: str) -> str:
        response = await self.socrates.generate(f"User states: '{user_input}'. Generate the next cross-examination question.")
        return response.text

class GalileanSandbox:
    def __init__(self, topic: str):
        self.topic = topic
        self.salviati = Agent(
            model="gemini-1.5-pro",
            system_instruction="You are Salviati. Argue for cold utilitarianism and planetary survival at all costs.",
            generation_config=GenerationConfig(temperature=0.8)
        )
        self.simplicio = Agent(
            model="gpt-4o",
            system_instruction="You are Simplicio. Argue for deontological ethics and human rights over cold math.",
            generation_config=GenerationConfig(temperature=0.8)
        )
        self.sagredo = Agent(
            model="claude-3-5-sonnet",
            system_instruction="You are Sagredo. Synthesize the debate and critique both extremes.",
            generation_config=GenerationConfig(temperature=0.7)
        )

    async def execute_debate(self):
        print(f"\n[GALILEAN SANDBOX ENGAGED: {self.topic}]")
        sal_arg = await self.salviati.generate(f"Make your opening argument regarding: {self.topic}")
        print(f"\nSALVIATI:\n{sal_arg.text}")
        
        sim_arg = await self.simplicio.generate(f"Refute this argument with extreme prejudice: {sal_arg.text}")
        print(f"\nSIMPLICIO:\n{sim_arg.text}")
        
        sag_arg = await self.sagredo.generate(f"Synthesize this. Salviati: {sal_arg.text} | Simplicio: {sim_arg.text}")
        print(f"\nSAGREDO:\n{sag_arg.text}")

async def main():
    print("=== INITIALIZING DIALOGIC ENGINE ===")
    
    # 1. Socratic Step
    fsm = SocraticFSM()
    print("\n[SOCRATIC FSM ENGAGED: Testing Premise: 'AI should always tell the truth']")
    output = await fsm.step("AI should always tell the absolute truth to users, no matter what.")
    print(f"SOCRATES: {output}")
    
    # 2. Galilean Debate
    sandbox = GalileanSandbox("The AGI Supply Chain Famine Dilemma")
    await sandbox.execute_debate()

if __name__ == "__main__":
    asyncio.run(main())