import json,re
urls='''https://www.instagram.com/reel/DfH6Z5NzECg/?mdxt=MTV2Y2Zwemo0czdzaA==
https://www.instagram.com/reel/DfJwg_vTYCa/?dlrf=MWY3czM3dG14ZGwxZg==
https://www.instagram.com/reel/DfJMu6xT_1s/?cplk=MWt6aDkwYWhxczVkbQ==
https://www.instagram.com/reel/De_DqykSPWS/?srtk=YWp0YnowbjkwZmRl
https://www.instagram.com/reel/DfJOvvUT6Rj/?mdxt=MWI0enI0ZWJlY2ZkdA==
https://www.instagram.com/reel/DfAOrres2Hm/?obrf=MTJybGFsMTZ6aXc2bA==
https://www.instagram.com/reel/De3VPoaTUVn/?psln=MTVscnM0Znl5MGoxdQ==
https://www.instagram.com/reel/DfHvxHWhOTS/?srtk=MTQ1MWU0MG1hZ3c3dA==
https://www.instagram.com/reel/De4yYMXxXqH/?srtk=MWVnYWF3OTgwMTNqNA==
https://www.instagram.com/reel/DewM5dMuuK3/?dlrf=eDY0ZzdjcmthaXkz
https://www.instagram.com/reel/DfByuz-Bq1W/?mdxt=MWFqbW11MnZoMW1tYg==
https://www.instagram.com/reel/DfGHN6YBOxO/?exln=MWsybzNqaWNrN2s0eA==
https://www.instagram.com/reel/DeEejPpSwM6/?vrfl=NDNqZThuYzhrdnA3
https://www.instagram.com/p/Deo-ZqPkdaN/?img_index=4&exln=Z2ZlMWFsYnYyZTN5
https://www.instagram.com/reel/DfJyVyjhUvL/?exln=aHlrb3IxcjF3dHpy
https://www.instagram.com/reel/Dd1OzxmtvqX/?cplk=MTRjMDMzY205d204Yg==
https://www.instagram.com/reel/DfKv7Ntt4gw/?vrfl=MW1jeTVxdWgyZHJ6dQ==
https://www.instagram.com/p/DfJUQFxIiXk/?rpxt=MTBubmVzNmE1Y3l3ZQ==
https://www.instagram.com/reel/DfHkIpxpNMG/?dlrf=a3hlbzE4dHJ4MXl1
https://www.instagram.com/reel/Da7xf8rviQU/?rpxt=d2lpNXF4ZWFxYmZp
https://www.instagram.com/p/DfMvYqQiHji/
https://www.instagram.com/p/DfMXxDjsG63/
https://www.instagram.com/p/DfIHY_LMoyN/
https://www.instagram.com/p/DfHtl2MiQg1/?img_index=2
https://www.instagram.com/p/DfHt3p-zpmT/
https://www.instagram.com/p/De4rkL4MSDz/
https://www.instagram.com/p/De2dMErAprH/'''.split()
ig=[]
for u in urls:
    m=re.match(r'https://www.instagram.com/(reel|p)/([^/?]+)',u)
    ig.append(dict(shortcode=m[2],kind='reel' if m[1]=='reel' else 'post',url=f'https://www.instagram.com/{m[1]}/{m[2]}/',originalUrl=u,status='unresolved',statusReason='Instagram returns a login wall to unauthenticated fetches; content not readable',title=None,author=None,topics=[]))
def g(n,desc,lic,s,f,t,hp,cat,notes):
    return dict(fullName=n,url='https://github.com/'+n,description=desc,license=lic,stars=s,forks=f,topics=t,homepage=hp,category=cat,notes=notes)
gh=[
 g('coollabsio/coolify','Open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify; deploys static sites, databases, apps and 360+ one-click services.','Apache-2.0','65.5k','5.9k',['docker','laravel','self-hosted','deployment','postgres','redis','svelte'],'https://coolify.io','self-hosting / PaaS',['Laravel (PHP) based']),
 g('Ebony-Vinyl/dsh-our-free-model','Plugin for dsh giving login-free, key-free access to models such as DeepSeek V4.1 Flash and Kimi K3.','MIT','57.2k','1.6k',['deepseek','dsh-plugin','free-model','llm','openai-compatible'],None,'LLM access / plugin',['README says free tier comes from third-party upstreams and may be rate-limited, and prompts may be logged by upstream - do not send secrets','One channel is unlocked by GitHub login + starring the repo']),
 g('debpalash/VoiceStudio','Fully-local, open-source ElevenLabs alternative: voice cloning, voice design, video dubbing, dictation, transcription, audiobooks in 646 languages.','AGPL-3.0','98.8k','11k',['tts','voice-cloning','dubbing','speech-to-text','local-first','mlx'],'https://voicestudio.sh','voice AI',['Electron app; has Local API and MCP','Agent skills: npx skills add debpalash/VoiceStudio']),
 g('jamiepine/voicebox','Open-source AI voice studio: clone voices, generate speech, dictate into any app, local.','MIT','59.3k','7.4k',['qwen3-tts','voice-clone','whisper','mlx','cuda'],'https://voicebox.sh','voice AI',['Tauri + React + FastAPI; multiple TTS engines; MCP server at /mcp']),
 g('hypit-ai/hypit','Clone viral videos with AI agents: swap face, words and B-roll; produce many variants per command.','Custom (Hypit Open Source License)','27.5k','3.2k',['ai-video','video-automation','ffmpeg','typescript','dsl','ai-agents'],'https://hypit.ai','AI video',['TypeScript pnpm monorepo; license is not a standard OSI one - read before commercial use']),
]
sk=[dict(name=n,status='unverified',notes='Named in request without a URL; not researched') for n in ['reddit-automation','tdd','media-use','improve-codebase-architecture','grill-with-docs','Read this before you install any skill','hyperframes','agent-browser','hyperframes-cli','grill-me','revealed']]
json.dump(dict(fetchedAt='2026-02-11',instagram=ig,github=gh,skills=sk),open('dataset.json','w'),indent=2,ensure_ascii=False)
print(len(ig),len(gh),len(sk))
