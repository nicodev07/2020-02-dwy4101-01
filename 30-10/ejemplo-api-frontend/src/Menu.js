import { Navbar, Nav, NavDropdown } from 'react-bootstrap'

const MenuComponent = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="#home">Clavistel</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="#home">Inicio</Nav.Link>
                    <Nav.Link href="#link">Link</Nav.Link>
                    <NavDropdown title="Menu Navegación" id="basic-nav-dropdown">
                        <NavDropdown.Item href="#action/3.1">Acción 1</NavDropdown.Item>
                        <NavDropdown.Item href="#action/3.2">Acción 2</NavDropdown.Item>
                        <NavDropdown.Item href="#action/3.3">Acción 3</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="#action/3.4">Acción 4</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default MenuComponent