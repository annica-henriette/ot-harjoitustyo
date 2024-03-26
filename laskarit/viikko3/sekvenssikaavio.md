```mermaid
sequenceDiagram
    participant main
    
    main->>laitehallinto: HKLLaitehallinto()
    main->>rautaitetori: Lataajalaite()
    main->>ratikka6: Lukijalaite()
    main->>bussi244: Lukijalaite()
    main->>laitehallinto: lisaa_lataaja(rautatietori)
    main->>laitehallinto: lisaa_lukija(ratikka6)
    main->>laitehallinto: lisaa_lukija(bussi244)
```
