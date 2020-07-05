resource "azurerm_network_interface" "vn_netwwork_interface" {
  name                = "${var.vm_interface_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address}"
  }
}

resource "azurerm_linux_virtual_machine" "test_vm" {
  name                = "${var.vm_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "${var.vm_size}"
  admin_username      = "${var.vm_admin_username}"
  network_interface_ids = ["${azurerm_network_interface.vn_netwwork_interface.id}",]
  admin_ssh_key {
    username   = "${var.vm_admin_username}"
    public_key = "${file("~/.ssh/id_rsa.pub")}"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}
