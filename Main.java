public class Main {
    // Define particles
    public static class Particle {
        // Quantum numbers
        private Float mass, charge, spin;
        private String name;
        // Define quantum numbers
        public Particle(String name, Float mass, Float charge, Float spin) {
            this.mass = mass;
            this.charge = charge;
            this.spin = spin;
            this.name = name;
        }
        // Define the propagator
    }
    // Main
    public static void main(String[] args){
        // Define photon
        Particle photon = new Particle("Photon",0f,0f,1f);
        System.out.println(photon.name+" quantum numbers: Mass "+photon.mass+" GeV, Charge: "+ photon.charge +", Spin: "+ photon.spin);
        // Define electron
        Particle electron = new Particle("Electron",0.5f,-1f,0.5f);
        System.out.println(electron.name+" quantum numbers: Mass "+electron.mass+" GeV, Charge: "+ electron.charge +", Spin: "+ electron.spin);
        // Define positron
        Particle positron = new Particle("Positron",0.5f,1f,0.5f);
        System.out.println(positron.name+" quantum numbers: Mass "+positron.mass+" GeV, Charge: "+ positron.charge +", Spin: "+ positron.spin);
        // Define muon
        Particle muon = new Particle("Muon",105.7f,-1f,0.5f);
        System.out.println(muon.name+" quantum numbers: Mass "+muon.mass+" GeV, Charge: "+ muon.charge +", Spin: "+ muon.spin);
        // Define antimuon
        Particle antimuon = new Particle("Anti-muon",105.7f,1f,0.5f);
        System.out.println(antimuon.name+" quantum numbers: Mass "+antimuon.mass+" GeV, Charge: "+ antimuon.charge +", Spin: "+ muon.spin);
    }
}
