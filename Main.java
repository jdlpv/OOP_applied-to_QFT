public class Main {
    // Create Particles
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
    }
    // Main
    public static void main(String[] args){
        // Define electron
        Particle electron = new Particle("Electron",0.5f,-1f,0.5f);
        System.out.println(electron.name+" quantum numbers: Mass "+electron.mass+" eV, Charge: "+ electron.charge +", Spin: "+ electron.spin);
        // Define positron
        Particle positron = new Particle("Positron",0.5f,1f,0.5f);
        System.out.println(positron.name+" quantum numbers: Mass "+positron.mass+" eV, Charge: "+ positron.charge +", Spin: "+ positron.spin);
        // Define photon
        Particle photon = new Particle("Photon",0f,0f,1f);
        System.out.println(photon.name+" quantum numbers: Mass "+photon.mass+" eV, Charge: "+ photon.charge +", Spin: "+ photon.spin);
    }
}
