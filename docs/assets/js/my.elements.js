class MyHeader extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
            <!-- Header -->
            <header id="header"><a href="index.html" class="logo">MetPy</a></header>
        `
    }
}

customElements.define('my-header', MyHeader)

class MyFooter extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
            <!-- Footer -->
            <footer id="footer">
                <section class="split contact">
                    <section>
                        <h3>ABOUT ME</h3>
                        <p>Xandra Campo<br/>
                            Researcher at the Neutron Standards Laboratory (LPN)<br/>
                            Ionizing Radiation Metrology Laboratory (LMRI)<br/>
                            Research Centre for Energy, Environment and Technology (<a href="https://www.ciemat.es/portal.do">CIEMAT</a>)<br/>
                            xandra.campo@ciemat.com</p>
                    </section>
                    <section>
                        <h3>SOCIAL</h3>
                        <ul class="icons alt">
                            <li><a href="https://github.com/xandratxan" class="icon brands alt fa-github"><span class="label">GitHub</span></a>
                            </li>
                        </ul>
                    </section>
                </section>
            </footer>
        
            <!-- Copyright -->
            <div id="copyright">
                <ul>
                    <li>@ 2023, Xandra Campo</li>
                    <li>Design: <a href="https://html5up.net">HTML5 UP</a></li>
                    <li><a href="https://www.flaticon.com/" title="python icons">Icons: Freepik</a></li>
                </ul>
            </div>
        `
    }
}

customElements.define('my-footer', MyFooter)